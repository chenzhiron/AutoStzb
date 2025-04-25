import os
from datetime import datetime
from typing import Optional, List, Tuple

import cv2
import numpy as np
import pytz
from PIL import Image
from openpyxl import Workbook
from scipy.stats import truncnorm

# 常量定义
DATETIME_FORMAT = "%Y/%m/%d %H:%M:%S"
BEIJING_TIMEZONE = pytz.timezone("Asia/Shanghai")


def convert_to_timestamp(date_str: str, with_timezone: bool = False) -> Optional[float]:
    """将日期字符串转换为时间戳，支持附加时区信息"""
    try:
        if len(date_str) == 19 and " " not in date_str:  # 自动插入空格
            formatted_date_str = date_str[:10] + " " + date_str[10:]
        else:
            formatted_date_str = date_str
        dt = datetime.strptime(formatted_date_str, DATETIME_FORMAT)
        if with_timezone:
            dt = BEIJING_TIMEZONE.localize(dt)
        return dt.timestamp()
    except ValueError:
        return None


def get_current_timestamp() -> float:
    """获取当前时间的时间戳"""
    return datetime.now().timestamp()


def ensure_directory_exists(path: str):
    """确保指定路径的目录存在，如果不存在则创建"""
    if not os.path.exists(path):
        os.makedirs(path)


def export_excel(data: List[List], filename: str):
    """将数据导出为 Excel 文件"""
    wb = Workbook()
    ws = wb.active
    for row in data:
        ws.append(row)
    wb.save(f"{filename}.xlsx")


def save_error(d):
    """保存错误截图到指定目录"""
    current_path = os.getcwd()
    error_folder_path = os.path.join(current_path, "error")
    ensure_directory_exists(error_folder_path)

    date_folder_name = datetime.now().strftime("%Y-%m-%d")
    date_folder_path = os.path.join(error_folder_path, date_folder_name)
    ensure_directory_exists(date_folder_path)

    img_path = os.path.join(date_folder_path, f"{int(get_current_timestamp())}.png")
    d.screenshot().save(img_path)


def find_multiple_templates(
        main_img: np.ndarray,
        template: np.ndarray,
        threshold: float = 0.8,
        method: int = cv2.TM_CCOEFF_NORMED,
        offset_y: int = 200
) -> List[int]:
    """在主图像中查找多个模板匹配点的 y 坐标"""
    h, w = template.shape[:2]
    result = cv2.matchTemplate(main_img, template, method)
    match_locations = np.where(result <= threshold) if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] else np.where(
        result >= threshold)

    filtered_y_positions = []
    for pt in zip(*match_locations[::-1]):
        y = pt[1]
        if not filtered_y_positions or abs(y - filtered_y_positions[-1]) >= offset_y:
            filtered_y_positions.append(y)
    return filtered_y_positions


def pil_to_cv2(pil_img: Image.Image) -> np.ndarray:
    """将 PIL 图像转换为 OpenCV 格式"""
    pil_img = pil_img.convert("RGB")
    cv_img = np.array(pil_img)
    return cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)


def is_template_matched(big_image: Image.Image, small_image: np.ndarray, threshold: float = 0.01,
                        cvfn=cv2.TM_SQDIFF_NORMED) -> bool:
    """检查大图中是否匹配小图"""
    return is_template_matched_axis(big_image, small_image, threshold, cvfn) is not None


def preprocess_alpha_image(img_bgra: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """处理带透明通道的小图，返回 BGR 图和掩码"""
    alpha_mask = img_bgra[:, :, 3]
    _, mask = cv2.threshold(alpha_mask, 1, 255, cv2.THRESH_BINARY)
    img_bgr = img_bgra[:, :, :3].copy()
    img_bgr[alpha_mask == 0] = 0  # 透明区域置黑
    return img_bgr, mask


def is_template_matched_axis(
        big_image: Image.Image,
        small_image_cv: np.ndarray,
        threshold: float = 0.1,
        method=cv2.TM_SQDIFF_NORMED
) -> Optional[Tuple[Tuple[int, int], float]]:
    try:
        if not isinstance(small_image_cv, np.ndarray) or len(small_image_cv.shape) != 3:
            raise ValueError("small_image_cv 必须是 3 通道或 4 通道的 OpenCV 图像")

        big_image_cv = cv2.cvtColor(np.array(big_image), cv2.COLOR_RGB2BGR)

        if small_image_cv.shape[2] == 4:
            small_image_bgr, mask = preprocess_alpha_image(small_image_cv)
        else:
            small_image_bgr = small_image_cv
            mask = None

        res = cv2.matchTemplate(big_image_cv, small_image_bgr, method, mask=mask)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            min_val, _, min_loc, _ = cv2.minMaxLoc(res)
            print(f"[SQDIFF] 差异值: {min_val:.4f}, 位置: {min_loc}")
            return (min_loc, min_val) if min_val <= threshold else None
        else:
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            print(f"[CCORR/CCOEFF] 匹配值: {max_val:.4f}, 位置: {max_loc}")
            return (max_loc, max_val) if max_val >= threshold else None

    except Exception as e:
        print(f"匹配错误: {e}")
        return None


def find_top_template_matches(
        big_image: Image.Image,
        small_image_cv: np.ndarray,
        threshold: float = 0.1,
        max_results: int = 5,
        nms_threshold: float = 0.3
):
    try:
        if not isinstance(small_image_cv, np.ndarray) or len(small_image_cv.shape) != 3:
            raise ValueError("small_image_cv 必须是 3 通道或 4 通道的 OpenCV 图像")

        big_image_cv = cv2.cvtColor(np.array(big_image), cv2.COLOR_RGB2BGR)

        if small_image_cv.shape[2] == 4:
            small_image_bgr, mask = preprocess_alpha_image(small_image_cv)
        else:
            small_image_bgr = small_image_cv
            mask = None

        res = cv2.matchTemplate(big_image_cv, small_image_bgr, cv2.TM_SQDIFF_NORMED, mask=mask)

        locs = np.where(res <= threshold)
        matches = [((x, y), float(res[y, x])) for x, y in zip(*locs[::-1])]

        matches.sort(key=lambda x: x[1])

        if nms_threshold and len(matches) > 0:
            matches = apply_nms(matches, nms_threshold)

        return matches[:max_results]

    except Exception as e:
        print(f"匹配错误: {e}")
        return []


def apply_nms(matches, threshold: float):
    if len(matches) <= 1:
        return matches

    boxes = []
    scores = []
    h, w = matches[0][0][1], matches[0][0][0]

    for (x, y), diff in matches:
        boxes.append([x, y, x + w, y + h])
        scores.append(diff)

    indices = cv2.dnn.NMSBoxes(boxes, scores, score_threshold=0, nms_threshold=threshold)

    return [matches[i] for i in indices.flatten()]


def truncated_normal(min_val, max_val, mean=None, std=None, size=1):
    if min_val >= max_val:
        raise ValueError("max_val 必须大于 min_val")

    if mean is None:
        mean = (min_val + max_val) / 2
    else:
        mean = np.clip(mean, min_val, max_val)

    if std is None:
        std = (max_val - min_val) / 4

    a = (min_val - 0.5 - mean) / std
    b = (max_val + 0.4999 - mean) / std

    samples = truncnorm.rvs(a, b, loc=mean, scale=std, size=size)
    integers = np.round(samples).astype(int)
    integers = np.clip(integers, min_val, max_val)

    return integers[0] if size == 1 else integers.tolist()

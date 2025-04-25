import os
from datetime import datetime

import cv2
import numpy as np
import pytz
from PIL import Image
from openpyxl import Workbook
from scipy.stats import truncnorm

from typing import Optional, Tuple
import cv2
import numpy as np
from PIL import Image

def formatDate(date_str):
    try:
        # 格式化字符串，插入空格
        formatted_date_str = date_str[:10] + " " + date_str[10:]
        # 解析为 datetime 对象
        date_time_obj = datetime.strptime(formatted_date_str, "%Y/%m/%d %H:%M:%S")
        # 附加北京时区
        beijing_tz = pytz.timezone("Asia/Shanghai")
        date_time_obj = beijing_tz.localize(date_time_obj)
        # 将 datetime 对象转换为时间戳
        timestamp = date_time_obj.timestamp()
        return timestamp
    except:
        return None


def format_date_strptime(date_str):
    # 将字符串解析为 datetime 对象
    dt = datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")

    # 转换为时间戳
    timestamp = int(dt.timestamp())

    return timestamp


def get_formatted_time():
    # 获取当前时间
    now = datetime.now()

    return now.timestamp()


def export_excel(data: list[list], filename):
    # 创建一个新的工作簿
    wb = Workbook()
    ws = wb.active
    for v in data:
        # 插入数据
        ws.append(v)
    # 保存 Excel 文件
    wb.save(filename + ".xlsx")


def save_error(d):

    # 获取当前项目路径
    current_path = os.getcwd()

    # 设置 error 文件夹路径
    error_folder_path = os.path.join(current_path, "error")

    # 创建 error 文件夹，如果不存在
    if not os.path.exists(error_folder_path):
        os.mkdir(error_folder_path)

    # 设置当前日期的文件夹路径
    date_folder_name = datetime.now().strftime("%Y-%m-%d")
    date_folder_path = os.path.join(error_folder_path, date_folder_name)

    # 创建日期文件夹，如果不存在
    if not os.path.exists(date_folder_path):
        os.mkdir(date_folder_path)
    img_path = os.path.join(date_folder_path, str(get_formatted_time()) + ".png")
    d.screenshot().save(img_path)


def find_multiple_templates(
    main_img, template, threshold=0.8, method=cv2.TM_CCOEFF_NORMED, offset_y=200
):

    # 获取模板图像的尺寸
    h, w = template.shape[:2]

    # 使用模板匹配
    result = cv2.matchTemplate(main_img, template, method)
    # 根据阈值找到符合条件的所有匹配点
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        match_locations = np.where(
            result <= threshold
        )  # 对于 TM_SQDIFF，值越小匹配度越高
    else:
        match_locations = np.where(result >= threshold)
        
    filtered_y_positions = []
    for pt in zip(*match_locations[::-1]):  # 使用[::-1] 交换坐标顺序
        y = pt[1]

        # 如果过滤列表为空，直接添加第一个匹配点
        if not filtered_y_positions:
            filtered_y_positions.append(y)
        else:
            # 只添加与最后一个 y 坐标距离超过 min_distance 的 y 坐标
            if abs(y - filtered_y_positions[-1]) >= offset_y:
                filtered_y_positions.append(y)
    return filtered_y_positions  # 返回 y 坐标列表


def pil_to_cv2(pil_img):
    # 将 PIL 图像转换为 RGB 模式（如果不是 RGB 模式）
    pil_img = pil_img.convert("RGB")
    # 转换为 numpy 数组
    cv_img = np.array(pil_img)
    # 将颜色通道从 RGB 转为 BGR 以适配 OpenCV
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    return cv_img




def is_template_matched(big_image: Image.Image, small_image: np.ndarray, threshold: float = 0.01, cvfn=cv2.TM_SQDIFF_NORMED) -> bool:
    if is_template_matched_axis(big_image, small_image, threshold, cvfn) is None:
        return False
    return True

def preprocess_alpha_image(img_bgra: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """处理带透明通道的小图，返回BGR图和掩码"""
    alpha_mask = img_bgra[:, :, 3]
    _, mask = cv2.threshold(alpha_mask, 1, 255, cv2.THRESH_BINARY)
    img_bgr = img_bgra[:, :, :3].copy()
    img_bgr[alpha_mask == 0] = 0  # 透明区域置黑
    return img_bgr, mask
def is_template_matched_axis(
        big_image: Image.Image,
        small_image_cv: np.ndarray,
        threshold: float = 0.1,  # 默认阈值需根据实际情况调整
        method=cv2.TM_SQDIFF_NORMED
) -> Optional[Tuple[Tuple[int, int], float]]:
    """
    通用的模板匹配函数，支持所有OpenCV匹配方法
    :param big_image: PIL格式的大图
    :param small_image_cv: OpenCV格式的小图（BGR或BGRA）
    :param threshold: 匹配阈值（根据方法类型调整）
    :param method: OpenCV匹配方法（如cv2.TM_CCOEFF_NORMED）
    :return: (匹配位置(x,y), 匹配值) 或 None
    """
    try:
        # 输入检查
        if not isinstance(small_image_cv, np.ndarray) or len(small_image_cv.shape) != 3:
            raise ValueError("small_image_cv 必须是3通道或4通道的OpenCV图像")

        # 转换大图为OpenCV BGR格式
        big_image_cv = cv2.cvtColor(np.array(big_image), cv2.COLOR_RGB2BGR)

        # 预处理小图（支持透明通道）
        if small_image_cv.shape[2] == 4:
            small_image_bgr, mask = preprocess_alpha_image(small_image_cv)
        else:
            small_image_bgr = small_image_cv
            mask = None

        # 执行模板匹配
        res = cv2.matchTemplate(big_image_cv, small_image_bgr, method, mask=mask)

        # 根据方法类型选择极值
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            # 取最小值（值越小越匹配）
            min_val, _, min_loc, _ = cv2.minMaxLoc(res)
            print(f"[SQDIFF] 差异值: {min_val:.4f}, 位置: {min_loc}")
            return (min_loc, min_val) if min_val <= threshold else None
        else:
            # 取最大值（值越大越匹配）
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
    """
    返回匹配差异值 <= threshold 的Top5结果（按差异值升序排列）
    :param big_image: PIL格式的大图
    :param small_image_cv: OpenCV格式的小图（BGR或BGRA）
    :param threshold: 差异阈值（TM_SQDIFF_NORMED，越小越匹配）
    :param max_results: 最多返回的结果数（默认5）
    :param nms_threshold: 非最大值抑制阈值（抑制重叠框）
    :return: [((x1,y1), diff1), ((x2,y2), diff2), ...]，最多5个
    """
    try:
        # 检查输入
        if not isinstance(small_image_cv, np.ndarray) or len(small_image_cv.shape) != 3:
            raise ValueError("small_image_cv 必须是3通道或4通道的OpenCV图像")

        # 转换大图为OpenCV BGR格式
        big_image_cv = cv2.cvtColor(np.array(big_image), cv2.COLOR_RGB2BGR)

        # 预处理小图（支持透明通道）
        if small_image_cv.shape[2] == 4:
            small_image_bgr, mask = preprocess_alpha_image(small_image_cv)
        else:
            small_image_bgr = small_image_cv
            mask = None
        res = cv2.matchTemplate(
            big_image_cv, small_image_bgr,
            cv2.TM_SQDIFF_NORMED, mask=mask
        )

        locs = np.where(res <= threshold)
        matches = [ ((x, y), float(res[y, x])) for x, y in zip(*locs[::-1]) ]

        # 按差异值升序排序（差异越小越匹配）
        matches.sort(key=lambda x: x[1])

        # 非最大值抑制（NMS）去除重叠区域
        if nms_threshold and len(matches) > 0:
            matches = apply_nms(matches, nms_threshold)

        # 返回前max_results个结果（最多5个）
        return matches[:max_results]

    except Exception as e:
        print(f"匹配错误: {e}")
        return []


def apply_nms(
    matches,
    threshold: float
):
    """
    非最大值抑制（NMS）过滤重叠匹配
    :param matches: [((x,y), diff), ...]
    :param threshold: 重叠阈值（IoU）
    :return: 过滤后的匹配点
    """
    if len(matches) <= 1:
        return matches

    # 提取坐标和差异值
    boxes = []
    scores = []
    h, w = matches[0][0][1], matches[0][0][0]  # 假设小图尺寸一致

    for (x, y), diff in matches:
        boxes.append([x, y, x + w, y + h])
        scores.append(diff)

    # 使用OpenCV的NMS
    indices = cv2.dnn.NMSBoxes(
        boxes, scores,
        score_threshold=0,
        nms_threshold=threshold
    )

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

    if size == 1:
        return int(integers[0])
    else:
        return [int(x) for x in integers]
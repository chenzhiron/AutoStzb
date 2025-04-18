import os
from datetime import datetime

import cv2
import numpy as np
import pytz
from PIL import Image
from openpyxl import Workbook
from scipy.stats import truncnorm


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

    # # 在主图像上绘制匹配矩形框
    # matched_img = main_img.copy()
    # for pt in zip(*match_locations[::-1]):  # 使用[::-1] 交换坐标顺序
    #     top_left = pt
    #     bottom_right = (top_left[0] + w, top_left[1] + h)
    #     cv2.rectangle(matched_img, top_left, bottom_right, (0, 255, 0), 2)

    # # 显示结果
    # plt.figure(figsize=(10, 5))
    # plt.imshow(cv2.cvtColor(matched_img, cv2.COLOR_BGR2RGB))
    # plt.title('Multiple Matched Regions')
    # plt.axis('off')
    # plt.show()

    # return match_locations


def pil_to_cv2(pil_img):
    # 将 PIL 图像转换为 RGB 模式（如果不是 RGB 模式）
    pil_img = pil_img.convert("RGB")
    # 转换为 numpy 数组
    cv_img = np.array(pil_img)
    # 将颜色通道从 RGB 转为 BGR 以适配 OpenCV
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    return cv_img




def is_template_matched(big_image: Image.Image, small_image_path: str, threshold: float = 0.95) -> bool:
    """
    在大图中匹配小图，如果相似度达到阈值则返回True，否则返回False

    参数:
        big_image: PIL.Image.Image类型的大图
        small_image_path: 小图的本地文件路径
        threshold: 相似度阈值，默认为0.95(95%)

    返回:
        bool: 是否匹配成功
    """
    try:
        # 将PIL.Image转换为OpenCV格式(BGR)
        big_image_cv = cv2.cvtColor(np.array(big_image), cv2.COLOR_RGB2BGR)

        # 读取小图
        small_image_cv = cv2.imread(small_image_path, cv2.IMREAD_COLOR)
        if small_image_cv is None:
            raise ValueError(f"无法读取小图: {small_image_path}")

        # 获取小图尺寸
        h, w = small_image_cv.shape[:2]

        # 进行模板匹配
        res = cv2.matchTemplate(big_image_cv, small_image_cv, cv2.TM_CCOEFF_NORMED)

        # 获取最大匹配值
        max_val = np.max(res)

        # 判断是否达到阈值
        return max_val >= threshold

    except Exception as e:
        print(f"匹配过程中发生错误: {e}")
        return False


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
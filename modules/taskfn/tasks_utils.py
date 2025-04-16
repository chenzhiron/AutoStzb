import cv2
import numpy as np

from modules.devices.main import Devices
from modules.ocr.main import ocr_format_val
from modules.utils import formatDate
from datetime import datetime
import re

def battle_time(img, v):
    # 战报时间
    times = formatDate(
        ocr_format_val(np.array(img.crop([665, v + 240, 900, v + 240 + 40])))
    ) or formatDate(
        ocr_format_val(np.array(img.crop([665, v + 230, 900, v + 230 + 50])))
    )
    if type(times) is str or times is None:
        times = formatDate(
            ocr_format_val(
                np.array(img.crop([665, v + 230 + 80, 900, v + 230 + 80 + 60]))
            )
        )
    print("times", times)
    return times

def time_str_to_seconds(time_str):
    try:
        time_obj = datetime.strptime(time_str, '%H:%M:%S')
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds
    except (ValueError, AttributeError, TypeError):
        return 0

def time_consuming(data):
    result = []
    for v in data[0]:
        custom_times = v[1][0]
        result.append(time_str_to_seconds(custom_times))
    return max(result)


def extract_numbers_from_brackets(text):
    # 使用正则表达式查找括号内的内容
    match = re.search(r'[（(]([^）)]+)[）)]', text)
    if not match:
        return None

    # 获取括号内的内容
    content = match.group(1)

    # 使用非数字分割字符串
    numbers = re.split(r'[^\d]+', content)

    # 过滤掉空字符串并转换为整数
    numbers = [int(num) for num in numbers if num]

    # 如果找到至少两个数字，返回前两个
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        return None

class BaseTypeImg:
    def __init__(self):
        self.attack_template_img = cv2.imread(
            "./modules/imgs/attack_template.png", cv2.IMREAD_COLOR
        )
        self.defense_template_img = cv2.imread(
            "./modules/imgs/defense_template.png", cv2.IMREAD_COLOR
        )
        self.exploit_template_img = cv2.imread(
            "./modules/imgs/condinate.png", cv2.IMREAD_COLOR
        )


class BaseReturnMain:
    def __init__(self, d:Devices):
        self.device = d
    def return_main(self):
        pass
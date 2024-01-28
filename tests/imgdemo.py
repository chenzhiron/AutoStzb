import time

import cv2
import numpy as np
from PIL import Image

from tests.config.config import globalConfig
from tests.devices.device import Devices
from ocr.main import ocrDefault

import cv2
from PIL import ImageGrab


def match_template_and_save_result(screenshot_path, template_path, result_path):
    # 读取屏幕截图和模板图像
    original_image = cv2.imread(screenshot_path)
    template = cv2.imread(template_path)

    # 如果需要，确保模板的维度小于原始图像的维度
    if original_image.shape[0] < template.shape[0] or original_image.shape[1] < template.shape[1]:
        raise ValueError("Template image should not be larger than the original image.")

    # 将图像转换为灰度图，有助于模板匹配
    gray_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 在原始图像中进行模板匹配
    result = cv2.matchTemplate(gray_original, gray_template, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果的坐标
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if max_val < 0.8:  # 可以调整阈值，以便于确定匹配的准确度
        print("No match found with enough confidence.")
        return False

    # 在原始图像上绘制匹配的区域
    top_left = max_loc
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    cv2.rectangle(original_image, top_left, bottom_right, (0, 255, 0), 2)

    # 保存匹配结果
    cv2.imwrite(result_path, original_image)
    print(f"Template matched and result saved to {result_path}")
    return True


device = Devices(globalConfig)
area = (444, 628, 462, 660)
# 主程序入口
if __name__ == '__main__':
    try:
        device.startDevices()
        img = device.getScreenshots()
        img.crop(area).save('9.png')
        # 示例：你可以根据需要更改路径
        screenshot_path = '9.png'
        template_path = '1.png'
        result_path = 'result.png'

        # 如果你需要从设备直接获取截图，你可以使用PIL中的ImageGrab
        img = ImageGrab.grab()
        img.save(screenshot_path)

        # 进行模板匹配并保存结果
        match_template_and_save_result(screenshot_path, template_path, result_path)
        device.closeDevice()
    except Exception as e:
        print(f"An error occurred: {e}")

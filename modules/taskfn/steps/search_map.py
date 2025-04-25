import time

import numpy as np

from modules.imgs.img_path import ImgNames
from modules.ocr.main import ocr_format_val
from modules.taskfn.basic import Basic
from modules.taskfn.tasks_utils import extract_numbers_from_brackets
from modules.utils import is_template_matched, truncated_normal


class SearchMap(Basic):
    def click_jump_map(self):
        self.current_screenshot = self.device.screenshot()
        if is_template_matched(self.current_screenshot, ImgNames.get_image(ImgNames.SEARCH)):
            self.device.click(1420, 95)
            return True
        else:
            self.device.click(1428, 104)
            time.sleep(3)
            self.device.click(1420, 95)
            return True

    def click_map_axis(self):
        self.current_screenshot = self.device.screenshot()
        ocr_text = ocr_format_val(np.array(self.current_screenshot.crop([1410, 835, 1580, 885])))
        if ocr_text == '跳转':
            self.device.click(truncated_normal(1160, 1245), 855)
            time.sleep(1)
            self.device.input(str(self.config['x']), True)
            self.device.click(truncated_normal(200, 1400), truncated_normal(100, 600))
            time.sleep(1)
            self.device.click(truncated_normal(1290, 1360), 855)
            time.sleep(1)
            self.device.input(str(self.config['y']), True)
            self.device.click(truncated_normal(200, 1400), truncated_normal(100, 600))
            time.sleep(1)
            self.device.click(truncated_normal(1410, 1580), truncated_normal(835, 885))
            return True

    def click_verify_address(self):
        self.device.click(800, 460)
        time.sleep(1)
        self.current_screenshot = self.device.screenshot()
        ocr_result = ocr_format_val(np.array(self.current_screenshot.crop([675, 350, 930, 390])))
        address_result = extract_numbers_from_brackets(ocr_result)
        if address_result is None:
            return False
        if address_result[0] == int(self.config['x']) and address_result[1] == int(self.config['y']):
            return True

    def execute_search_map(self):
        steps = [
            self.click_jump_map,
            self.click_map_axis,
            self.click_verify_address,
        ]
        self.execute_steps(steps)
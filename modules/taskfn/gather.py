import time

import numpy as np

from modules.devices.main import Devices
from modules.imgs.img_path import ImgNames
from modules.ocr.main import ocrnormal, ocr_format_val
from modules.taskfn.tasks_utils import time_consuming, BaseReturnMain
from modules.utils import is_template_matched, truncated_normal


class Gather(BaseReturnMain):
    def __init__(self, device:Devices, config, db = None):
        super().__init__(device)
        self.config = {
            'address': '',
            'num': 1
        }
        self.db = db
        self.current_screenshot = None
        self.result = {}
    def action_click(self, img_path: str):
        self.current_screenshot = self.device.screenshot()
        if is_template_matched(self.current_screenshot, ImgNames.get_path(img_path)):
            self.device.click(truncated_normal(375, 440), truncated_normal(735, 880))
            return True
        return False
    def action_list(self, img_path:str):
        self.current_screenshot = self.device.screenshot()
        if is_template_matched(self.current_screenshot,ImgNames.get_path(img_path)):
            if self.config['address'] == '':
                num = self.config['num']
                offset_x = 75 + ((170 + 40) * (num -1))
                offset_x_end =  75 + (170 * num) + (40 * (num -1))
                offset_y = 240 + 80
                offset_y_end = offset_y + 80
                print(offset_x, offset_x_end, offset_y, offset_y_end)
                self.device.click(truncated_normal(offset_x,offset_x_end), truncated_normal(offset_y, offset_y_end))

    def action_zhengbing(self, img_paths:list[str]):
        self.current_screenshot = self.device.screenshot()
        state = False
        for v in img_paths:
            if is_template_matched(self.current_screenshot, ImgNames.get_path(v)):
                state = True
                break
        if state:
            self.device.click(truncated_normal(735, 850), truncated_normal(665,720))

    def action_zhengbing_max(self, img_path:str):
        self.current_screenshot = self.device.screenshot()
        if is_template_matched(self.current_screenshot, ImgNames.get_path(img_path)):
            self.device.click(truncated_normal(1135,1280), truncated_normal(825,860))

    def action_max_time(self):
        self.current_screenshot = self.device.screenshot()
        time_result = ocrnormal(np.array(self.current_screenshot.crop([872,490,980, 815])))
        max_time = time_consuming(time_result)
        self.result.update({
            "time_consuming": max_time
        })

    def action_click_confirm(self):
        self.device.click(truncated_normal(1325,1550), truncated_normal(825,860))

    def action_click_confirm_end(self):
        self.current_screenshot = self.device.screenshot()
        confirm_text = ocr_format_val(np.array(self.current_screenshot.crop([860,570,1080,614])))
        if confirm_text == '确定':
            self.device.click(truncated_normal(860,1080), truncated_normal(570,614))
            return True
        return False


    def execute(self):
        self.action_click(ImgNames.SHILI)
        time.sleep(5)
        self.action_list(ImgNames.SHILIPAGE)
        time.sleep(5)
        self.action_zhengbing([ImgNames.ZHENGBING, ImgNames.ZHENGBINGING])
        time.sleep(5)
        self.action_zhengbing_max(ImgNames.ZHENGBINGMAX)
        time.sleep(5)
        self.action_max_time()
        time.sleep(5)
        self.action_click_confirm()
        time.sleep(5)
        self.action_click_confirm_end()

if __name__=='__main__':
    d = Devices('127.0.0.1:16384')
    gather = Gather(d, {})
    gather.execute()
    print(gather.result)
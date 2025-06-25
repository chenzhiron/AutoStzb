from functools import wraps

import cv2
import numpy as np

from modules.devices.main import DeviceOperator
from modules.imgs.img_path import ImgNames
from modules.ocr.main import ocr_format_val, ocr_format_list, ocr_normal
from modules.taskfn.tasks_utils import process_list
from modules.utils import is_template_matched, is_template_matched_axis


class StepsBasic:
    def __init__(self, device: DeviceOperator):
        self.screenshot = None
        self.device = device

    def refresh(self):
        self.screenshot = self.device.screenshot()

    def auto_refresh(func):
        """自动刷新截图的装饰器"""

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if kwargs.pop('refresh', True):  # 默认刷新，但允许手动关闭
                self.refresh()
            return func(self, *args, **kwargs)

        return wrapper

    @auto_refresh
    def verify_action_click(self):
        return is_template_matched(self.screenshot, ImgNames.get_image(ImgNames.SHILI))

    @auto_refresh
    def verify_action_list(self):
        return is_template_matched(self.screenshot, ImgNames.get_image(ImgNames.SHILIPAGE), 0.9,
                                   cv2.TM_CCORR_NORMED)

    @auto_refresh
    def verify_going_zhengbing(self):
        for v in [ImgNames.ZHENGBING, ImgNames.ZHENGBINGING]:
            if is_template_matched(self.screenshot, ImgNames.get_image(v), 0.9, cv2.TM_CCORR_NORMED):
                return True
        return False

    @auto_refresh
    def verify_zhengbing_page(self):
        return is_template_matched(self.screenshot, ImgNames.get_image(ImgNames.ZHENGBINGMAX))

    @auto_refresh
    def verify_zhengbing_max_time(self):
        return ocr_normal(np.array(self.screenshot.crop([872, 490, 980, 815])))

    @auto_refresh
    def verify_click_confirm_end(self):
        return ocr_format_val(np.array(self.screenshot.crop([860, 570, 1080, 614])))

    @auto_refresh
    def verify_click_jump_map(self):
        return is_template_matched(self.screenshot, ImgNames.get_image(ImgNames.SEARCH))

    @auto_refresh
    def verify_click_map_axis(self):
        return ocr_format_val(np.array(self.screenshot.crop([1410, 835, 1580, 885])))

    @auto_refresh
    def verify_click_address(self):
        return ocr_format_val(np.array(self.screenshot.crop([675, 350, 950, 390])))

    @auto_refresh
    def verify_go_map(self, repeat=False):
        imgName = ImgNames.JINGON if repeat else ImgNames.SAODANG
        return is_template_matched_axis(self.screenshot.crop([550, 200, 1220, 800]),
                                        ImgNames.get_image(imgName), 0.15)

    @auto_refresh
    def verify_select_list_action(self, **kwargs):
        distance = ocr_format_val(np.array(self.screenshot.crop([1235, 195, 1415, 250])))
        return distance

    @auto_refresh
    def verify_process_list(self, **kwargs):
        list_max = process_list(ocr_format_list(np.array(self.screenshot.crop([300, 800, 1410, 835]))))
        return list_max

    @auto_refresh
    def verify_delay_time(self):
        return ocr_format_val(np.array(self.screenshot.crop([770, 650, 883, 690])))

    @auto_refresh
    def verify_search_map_address(self):
        return is_template_matched_axis(self.screenshot.crop([340, 220, 1220, 715]),
                                        ImgNames.get_image(ImgNames.ADDRESS), 0.8,
                                        cv2.TM_CCORR_NORMED)

    @auto_refresh
    def verify_map_action_result(self):
        return ocr_format_val(np.array(self.screenshot.crop([665, 240, 880, 425])))

    @auto_refresh
    def verify_my_remaining(self):
        return ocr_format_val(np.array(self.screenshot.crop([60, 230, 250, 273])))

    @auto_refresh
    def verify_enemy_remaining(self):
        return ocr_format_val(np.array(self.screenshot.crop([1315, 230, 1485, 273])))

    @auto_refresh
    def verify_draw_run(self):
        return is_template_matched_axis(self.screenshot.crop([1240, 220, 1590, 720]),
                                        ImgNames.get_image(ImgNames.DRAWRUN), 0.9,
                                        cv2.TM_CCORR_NORMED)

    @auto_refresh
    def verify_draw_run_time(self):
        return ocr_format_val(np.array(self.screenshot.crop([770, 670, 885, 715])))

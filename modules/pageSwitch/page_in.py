import time

import numpy as np

from device.automation import get_screenshots
from device.operate import operate_adb_tap, operate_adb_swipe
from modules.general.generalExecuteFn import executeClickArea, calculate_max_timestamp
from modules.general.module_options_name import shili, zhengbing, require_zhengbing, zhengbing_satisfy, queding
from modules.module_shili.address_area import shili_area
from modules.module_zhengbing.module_zhengbing_area import zhengbing_page_verify_area, click_list_x_y, \
    zhengbing_page_area, zhengbing_page_swipe_verify, zhengbing_page_swipe, zhengbing_time_area, queding_area
from ocr.main import ocr_default


def handle_in_map_conscription(l):
    times = 0
    while 1:
        try:
            time.sleep(0.3)
            image = get_screenshots()
            # 点击势力
            if appear_then_click(image.crop(shili_area), shili_area, [shili]):
                continue
            if appear_then_click(image.crop(zhengbing_page_verify_area),
                                 zhengbing_page_verify_area,
                                 [shili], False):
                x, y = click_list_x_y
                operate_adb_tap(x * l, y)
                continue
            if appear_then_click(image.crop(zhengbing_page_area), zhengbing_page_area, zhengbing):
                continue
            if appear_then_click(image.crop(zhengbing_page_swipe_verify), zhengbing_page_swipe_verify,
                                 [require_zhengbing, zhengbing_satisfy],
                                 False):
                for v in zhengbing_page_swipe:
                    operate_adb_swipe(v[0], v[1], v[2], v[3])
                time_res = ocr_default(np.array(image.crop(zhengbing_time_area)))
                result = [item[1][0] for sublist in time_res for item in sublist]
                times = calculate_max_timestamp(result)
                x, y = executeClickArea(zhengbing_page_swipe_verify)
                operate_adb_tap(x, y)
                continue
            if appear_then_click(image.crop(queding_area), queding_area, queding):
                return times
        except Exception as e:
            print('发生了错误', e)
            return None


def handle_out_map_conscription():
    pass


def appear_then_click(img_source, click_area, check_txt, clicked=True):
    res = ocr_default(np.array(img_source))
    if bool(res[0]):
        result = ''
        for sublist in res:
            for item in sublist:
                result += item[1][0]
        if result in check_txt:
            if clicked:
                x, y = executeClickArea(click_area)
                operate_adb_tap(x, y)
            return True
        else:
            return False
    else:
        return False

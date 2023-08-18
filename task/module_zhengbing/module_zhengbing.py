from PIL import Image
from path.img import path
from ocr.main import ocr_txt_zhengbing, ocr_default
from task.module_zhengbing.module_zhengbing_area import (zhengbing_page_area,
                                                         zhengbing_page_area_h,
                                                         zhengbing_page_area_w,
                                                         zhengbing_page_swipe,
                                                         zhengbing_page_queren_area,
                                                         zhengbing_page_queren_area_w,
                                                         zhengbing_page_queren_area_h,
                                                         zhengbing_time_area
                                                         )
from tools.reg_screenshot import general_screenshot_tools
from device.main import return_device
from tools.reg_time import reg_time
from tools.reg_coordinates import reg_coor

def module_zhengbing_click():
    device = return_device()
    if ocr_txt_zhengbing(path, '证兵', zhengbing_page_area):
        device.click(zhengbing_page_area_w / 2, zhengbing_page_area_h / 2)
        return True
    else:
        return False


def module_swipe_zhengbing_click():
    device = return_device()
    for v in zhengbing_page_swipe:
        device.swipe(sx=v[0], sy=v[1], ex=v[2], ey=v[3], duration=v[4])
    return True


def module_zhengbing_affirm_btn(auto_txt):
    device = return_device()
    if ocr_txt_zhengbing(path, auto_txt, zhengbing_page_queren_area):
        device.click(zhengbing_page_queren_area_w, zhengbing_page_queren_area_h)
    return True


def module_zhuangbing_time():
    device = return_device()
    general_screenshot_tools(zhengbing_time_area)
    res = ocr_default(path)
    max_time = []
    for v in res:
        if v['text'] != '确定':
            max_time.append(reg_time(v['text']))
    max_time.sort(reverse=True)
    x, y = reg_coor(res[-1]['position'])
    device.click(x, y)
    return True

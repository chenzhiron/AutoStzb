from device.main_device import return_device
from modules.module_zhengbing.module_zhengbing_area import (zhengbing_page_area,
                                                            zhengbing_page_area_h,
                                                            zhengbing_page_area_w,
                                                            zhengbing_page_swipe,
                                                            zhengbing_page_queren_area,
                                                            zhengbing_page_queren_area_w,
                                                            zhengbing_page_queren_area_h,
                                                            zhengbing_time_area,
                                                            zhengbing_time_queren_area
                                                            )
from ocr.main import ocr_txt_verify, ocr_default
from path.img import path
from tools.reg_coordinates import reg_coor
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_time import reg_time_2em


def module_zhengbing_click():
    device = return_device()
    time_number = 0
    while 1:
        if ocr_txt_verify(path, '证兵', zhengbing_page_area):
            device.click(zhengbing_page_area_w / 2, zhengbing_page_area_h / 2)
            return True
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('点击征兵，进入征兵进度条失败')


def module_swipe_zhengbing_click():
    device = return_device()
    time_number = 0
    while 1:
        if ocr_txt_verify(path, '确认证兵', zhengbing_page_queren_area):
            for v in zhengbing_page_swipe:
                device.swipe(sx=v[0], sy=v[1], ex=v[2], ey=v[3], duration=v[4])
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('拖动征兵进度条失败')


def module_zhengbing_affirm_btn(auto_txt):
    device = return_device()
    if ocr_txt_verify(path, auto_txt, zhengbing_page_queren_area):
        device.click(zhengbing_page_queren_area_w, zhengbing_page_queren_area_h)
    return True


def module_zhuangbing_time():
    device = return_device()
    time_number = 0
    while 1:
        if ocr_txt_verify(path, '确定', zhengbing_time_queren_area):
            general_screenshot_tools(zhengbing_time_area)
            res = ocr_default(path)
            max_time = []
            for v in res:
                if v['text'] != '确定':
                    max_time.append(reg_time_2em(v['text']))
            max_time.sort(reverse=True)
            print(max_time[0])
            x, y = reg_coor(res[-1]['position'])
            device.click(x, y)
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('征兵确认时间点击错误')

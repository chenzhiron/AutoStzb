from device.main_device import return_device
from modules.module_zhengbing.module_zhengbing_area import (zhengbing_page_area,
                                                            zhengbing_page_swipe,
                                                            zhengbing_page_queren_area,
                                                            zhengbing_page_queren_area_w,
                                                            zhengbing_page_queren_area_h,
                                                            zhengbing_time_area,
                                                            zhengbing_time_queren_area,
                                                            zhengbing_page_time_area
                                                            )
from ocr.main import ocr_txt_verify, ocr_default
from tools.reg_click_direction import reg_direction
from tools.reg_screenshot import general_screenshot_tools


def module_zhengbing_click(path, auto_txt='征兵'):
    time_number = 0
    while 1:
        if ocr_txt_verify(path, auto_txt, zhengbing_page_area):
            device = return_device()
            x, y = reg_direction(zhengbing_page_area)
            device.click(x, y)
            return True
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('点击征兵，进入征兵进度条失败')


def module_swipe_zhengbing_click(path, auto_txt='确认证兵'):
    time_number = 0
    while 1:
        if ocr_txt_verify(path, auto_txt, zhengbing_page_queren_area):
            for v in zhengbing_page_swipe:
                device = return_device()
                device.swipe(sx=v[0], sy=v[1], ex=v[2], ey=v[3], duration=v[4])
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('拖动征兵进度条失败')


def module_zhengbing_affirm_btn(path, auto_txt='确认证兵'):
    if ocr_txt_verify(path, auto_txt, zhengbing_page_queren_area):
        device = return_device()
        device.click(zhengbing_page_queren_area_w, zhengbing_page_queren_area_h)
    return True


def module_zhengbing_computed_time(path):
    general_screenshot_tools(zhengbing_page_time_area)
    # zhengbing_page_time_area 时间区域重新截图计算
    result = ocr_default(path)
    print(result)
    # 后续逻辑


def module_zhuangbing_time(path, auto_txt='确认'):
    time_number = 0
    while 1:
        # 确认 区域重新点击
        if ocr_txt_verify(path, auto_txt, zhengbing_time_queren_area):
            device = return_device()
            x, y = reg_direction(zhengbing_time_queren_area)
            device.click(x, y)
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('征兵确认时间点击错误')

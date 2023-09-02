import time

from device.main_device import connect_device, return_device
from modules.module_address.module_address_area import address_start_area_w, address_start_area_y, address_sign_area, \
    address_targe_w, address_targe_h, address_going_area, \
    address_going_list_time, address_result_area,address_going_targe_h,address_going_targe_w
from modules.module_duiwu.module_duiwu import module_click_chuzheng_duiwu
from ocr.main import ocr_default
from ocr.main import ocr_txt_verify
from config.img import path
from tools.reg_coordinates import reg_coor
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_time import reg_time

import logging


def module_address_start():
    device = connect_device()
    device.click(address_start_area_w, address_start_area_y)
    time_number = 0
    while 1:
        if ocr_txt_verify(path, '标记', address_sign_area):
            device.click(address_targe_w, address_targe_h)
            time.sleep(0.5)
            device.click(address_going_targe_w, address_going_targe_h)
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('标记土地选择异常')


def module_address_going(auto_txt='扫荡'):
    device = return_device()
    time_number = 1
    while 1:
        general_screenshot_tools(address_going_area)
        result = ocr_default(path)
        if len(result) != 0:
            if result[0]['text'] == auto_txt:
                x, y = reg_coor(result[0]['position'])
                device.click(x, y)
                break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('土地选择异常')


def module_address_list_going(i):
    if int(i) == 0:
        raise Exception('队伍选择异常')
    device = return_device()
    module_click_chuzheng_duiwu(i)
    while 1:
        if ocr_txt_verify(path, '扫荡', address_result_area):
            general_screenshot_tools(address_going_list_time)
            result = ocr_default(path)
            if len(result[0]['text']) != 0:
                times = reg_time(result[0]['text'])
                # logging.info(times)
                general_screenshot_tools(address_result_area)
                while 1:
                    end = ocr_default(path)
                    x, y = reg_coor(end[0]['position'])
                    device.click(x, y)
                    return times
                break


if __name__ == '__main__':
    connect_device()
    module_address_start()
    # module_address_going()
    module_address_start()
    # module_address_going()
    # module_address_list_going(3)
    # module_address_start()
    # module_address_going()
    # module_address_list_going(4)
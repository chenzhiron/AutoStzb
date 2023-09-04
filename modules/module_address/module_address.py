import time

from config.img import path
from device.main_device import connect_device, return_device
from modules.module_address.module_address_area import address_start_area_w, address_start_area_y, address_sign_area, \
    address_targe_w, address_targe_h, address_going_area, \
    address_going_list_time, address_result_area, address_going_targe_h, address_going_targe_w, address_saodang, \
    address_chuzheng, address_affirm_button
from modules.module_duiwu.module_duiwu import module_click_chuzheng_duiwu
from ocr.main import ocr_default
from ocr.main import ocr_txt_verify
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_time import reg_time


def module_address_start():
    device = connect_device()
    time_number = 50
    # 假设还没有进行过点击
    device.click(address_start_area_w, address_start_area_y)
    while time_number > 0:
        if ocr_txt_verify(path, '标记', address_sign_area):
            device.click(address_targe_w, address_targe_h)
            time.sleep(0.5)
            device.click(address_going_targe_w, address_going_targe_h)
            break
        else:
            time_number -= 1
    if time_number <= 0:
        raise Exception('标记土地选择异常')


def module_address_going(auto_txt='扫荡'):
    device = return_device()
    time_number = 50
    while time_number > 0:
        general_screenshot_tools(address_going_area)
        text = ocr_default(path)
        if len(text) > 0 and auto_txt in text:
            if auto_txt == '扫荡':
                x, y = address_saodang
                device.click(x, y)
                break
            elif auto_txt == '出征':
                x, y = address_chuzheng
                device.click(x, y)
                break
            else:
                time_number -= 1
        else:
            time_number -= 1
    if time_number <= 0:
        raise Exception('选择异常:::::' + auto_txt)


def module_address_list_going(i):
    if 0 >= int(i) > 5:
        raise Exception('队伍选择异常')
    device = return_device()
    module_click_chuzheng_duiwu(i)
    while 1:
        if ocr_txt_verify(path, '扫荡', address_result_area):
            general_screenshot_tools(address_going_list_time)
            result = ocr_default(path)
            if result != 0:
                times = reg_time(result)
                print(times)
                x, y = address_affirm_button
                device.click(x, y)
                return times


# if __name__ == '__main__':
#     connect_device()
#     module_address_start()
#     module_address_going()
#     module_address_list_going(4)
#     module_address_start()
#     module_address_going()
#     module_address_list_going(5)

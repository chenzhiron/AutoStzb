import time

from device.main_device import return_device
from modules.module_duiwu.module_duiwu import module_click_chuzheng_duiwu
from modules.module_going.module_going_area import address_area_time_arrive, add_demo_area, chuzheng_btn_area
from ocr.main import ocr_default, ocr_txt_click
from config.img import path
from tools.reg_coordinates import reg_coor
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_time import reg_time


def chuzheng(auto_txt = '扫荡', i = 1):
    d = return_device()
    x, y = add_demo_area
    d.click(x, y)
    time.sleep(1)
    d.screenshot().save(path)
    ocr_txt_click(path, auto_txt)
    module_click_chuzheng_duiwu(i)
    time.sleep(1)
    general_screenshot_tools(address_area_time_arrive)
    res = ocr_default(path)
    times = reg_time(res[0]['text'])
    print(times)
    general_screenshot_tools(chuzheng_btn_area)
    v = ocr_default(path)
    if v[0]['text'] == auto_txt:
        x2, y2 = reg_coor(v[0]['position'])
        d.click(x2, y2)

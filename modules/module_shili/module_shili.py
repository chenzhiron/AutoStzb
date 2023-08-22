from modules.module_shili.address_area import area
from ocr.main import ocr_v3
from tools.reg_list_name import group_txt_click
from tools.reg_screenshot import general_screenshot_tools


def module_click_shili(path, auto_text):
    time_number = 0
    while 1:
        general_screenshot_tools(area)
        list_txt = ocr_v3(path)
        if group_txt_click(list_txt, auto_text):
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('点击势力页面失败')

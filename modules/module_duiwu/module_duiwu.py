from ocr.main import ocr_txt_click, ocr_txt_v3
from ocr.ocr_model_name import vertical_model_name
from modules.module_duiwu.address_area import list_name_area, list_click_area
from tools.reg_list_name import reg_list_name
from tools.team_direction import chuzheng_direction, zhengbing_direction
from ocr.main import ocr_txt_zhengbing
from tools.reg_screenshot import general_screenshot_tools
from device.main import return_device


def module_click_chuzheng_duiwu(i):
    x, y = chuzheng_direction(i)
    device = return_device()
    device.click(x, y)


def module_click_zhengbing_duiwu(i):
    x, y = zhengbing_direction(i)
    device = return_device()
    device.click(x, y)
    return True


def module_reg_zhengbing_page(path):
    return ocr_txt_zhengbing(path, (0, 0, 240, 88), '势力')

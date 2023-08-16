import path.img
from ocr.main import ocr_txt_click, ocr_txt_v3
from ocr.ocr_model_name import vertical_model_name
from task.module_duiwu.address_area import list_name_area, list_click_area
from tools.reg_list_name import reg_list_name
from tools.team_direction import chuzheng_direction, zhengbing_direction
from ocr.main import ocr_txt_zhengbing


def module_ocr_duiwu_name(device, path, is_main=False):
    area = list_name_area,
    if is_main:
        area = list_click_area
    device.screenshot().crop(area).save(path)
    result = ocr_txt_v3(path)
    return reg_list_name(result)


def module_click_duiwu(device, path, auto_txt, is_main=False):
    area = list_name_area
    if is_main:
        area = list_click_area
    device.screenshot().save(path)
    return ocr_txt_click(path, auto_txt, vertical_model_name, area, True)


def module_click_chuzheng_duiwu(device, i):
    x, y = chuzheng_direction(i)
    device.click(x, y)


def module_click_zhengbing_duiwu(device, i):
    x, y = zhengbing_direction(i)
    print(x, y)
    device.click(x, y)
    return True


def module_reg_zhengbing_page(path):
    return ocr_txt_zhengbing(path, (0, 0, 240, 88), '势力')

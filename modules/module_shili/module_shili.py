from modules.module_shili.address_area import area
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_list_name import group_txt_click
from ocr.main import ocr_v3


def module_click_shili(path, auto_text):
    general_screenshot_tools(area)
    list_txt = ocr_v3(path)
    return group_txt_click(list_txt, auto_text)

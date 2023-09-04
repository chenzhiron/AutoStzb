from device.main_device import return_device
from modules.modules_start.module_start_area import start_area
from ocr.main import ocr_txt_verify
from tools.reg_click_direction import reg_direction


def module_click_start(path, auto_text='开始游戏'):
    if ocr_txt_verify(path, auto_text, start_area):
        device = return_device()
        x, y = reg_direction(start_area)
        device.click(x, y)
        return True

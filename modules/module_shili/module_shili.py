import time

from config.const import TIMESLEEP
from config.paths import path

from device.main_device import return_device,connect_device
from modules.general.module_error_txt import click_shili_error
from modules.general.module_options_name import zhaomu
from modules.module_shili.address_area import shili_area, zhaomu_area
from ocr.main import ocr_txt_verify,ocr_default
from tools.reg_screenshot import general_screenshot_tools


def module_click_shili():
    time_number = 50

    # while time_number > 0:
    #     time.sleep(TIMESLEEP)
    #     if ocr_txt_verify(path, zhaomu, zhaomu_area):
    #         device = return_device()
    #         x, y = shili_area
    #         device.click(x, y)
    #         time.sleep(TIMESLEEP)
    #         break
    #     else:
    #         time_number -= 1
    # if time_number <= 0:
    #     raise Exception(click_shili_error)


if __name__ == '__main__':
    from config.paths import path
    device = connect_device()
    device.screenshot().save(path)
    general_screenshot_tools((375, 725, 445, 885))
    result = ocr_default(path)
    print(result)

    # module_click_shili()
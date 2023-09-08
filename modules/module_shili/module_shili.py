from config.img import path

from device.main_device import return_device
from modules.general.module_error_txt import click_shili_error
from modules.general.module_options_name import zhaomu
from modules.module_shili.address_area import shili_area, zhaomu_area
from ocr.main import ocr_txt_verify


def module_click_shili():
    time_number = 50
    while time_number > 0:
        if ocr_txt_verify(path, zhaomu, zhaomu_area):
            device = return_device()
            x, y = shili_area
            device.click(x, y)
            break
        else:
            time_number -= 1
    if time_number <= 0:
        raise Exception(click_shili_error)


# if __name__ == '__main__':
#     connect_device()
#     from config.img import path
#
#     module_click_shili(path)

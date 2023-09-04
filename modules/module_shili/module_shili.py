from device.main_device import return_device, connect_device
from modules.module_shili.address_area import shili_area, zhaomu
from ocr.main import ocr_txt_verify


def module_click_shili(img_path):
    time_number = 50
    while time_number > 0:
        if ocr_txt_verify(img_path, '招募', zhaomu):
            device = return_device()
            x, y = shili_area
            device.click(x, y)
            break
        else:
            time_number -= 1
    if time_number <= 0:
        raise Exception('点击势力页面失败')


# if __name__ == '__main__':
#     connect_device()
#     from config.img import path
#
#     module_click_shili(path)

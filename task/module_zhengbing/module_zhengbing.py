from PIL import Image
from path.img import path
from ocr.main import ocr_txt_zhengbing, ocr_default
from task.module_zhengbing.module_zhengbing_area import (zhengbing_page_area,
                                                         zhengbing_page_area_h,
                                                         zhengbing_page_area_w,
                                                         zhengbing_page_swipe,
                                                         zhengbing_page_queren_area,
                                                         zhengbing_time_area
                                                         )
def module_zhengbing_click(device):
    device.screenshot().crop(zhengbing_page_area).save(path)
    if ocr_txt_zhengbing(path, zhengbing_page_area, '证兵'):
        device.click(zhengbing_page_area_w / 2, zhengbing_page_area_h / 2)
        return True
    else:
        return False


def module_swipe_zhengbing_click(device):
    for v in zhengbing_page_swipe:
        device.swipe(sx=v[0], sy=v[1], ex=v[2], ey=v[3], duration=v[4])


def module_zhengbing_affirm_btn(path):
    res = ocr_txt_zhengbing(path, zhengbing_page_queren_area, '确认证兵')
    print(res)


def module_zhuangbing_time(device, path):
    Image.open(path).crop(zhengbing_time_area).save(path)
    res = ocr_default(path)
    print(res)

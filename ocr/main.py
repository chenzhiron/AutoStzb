from cnocr import CnOcr
from device.main import return_device

from tools.reg_coordinates import reg_coor


def orc_txt(img_path, auto_text):
    d = return_device()
    ocr = CnOcr()  # 所有参数都使用默认值
    out = ocr.ocr(img_path)
    for v in out:
        if v['text'] == auto_text:
            x, y = reg_coor(v['position'])
            d.click(x, y)
            return True
    return False


def orc_test(img_path):
    ocr = CnOcr()  # 所有参数都使用默认值
    out = ocr.ocr(img_path)
    return out

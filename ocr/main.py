from cnocr import CnOcr
from device.main import return_device

from tools.reg_coordinates import reg_coor


def ocr(img_path):
    orc = CnOcr()
    return orc.ocr(img_path)


def ocr_txt(img_path):
    return ocr(img_path)


def ocr_txt_click(img_path, auto_text):
    d = return_device()
    ocr = CnOcr()  # 所有参数都使用默认值
    out = ocr.ocr(img_path)
    for v in out:
        if v['text'] == auto_text:
            x, y = reg_coor(v['position'])
            d.click(x, y)
            return True
    return False

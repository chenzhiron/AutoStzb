from cnocr import CnOcr
from device.main import return_device
from tools.reg_coordinates import reg_coor
from tools.reg_list_name import reg_list_name
from PIL import Image
from tools.reg_screenshot import general_screenshot_tools


def ocr_default(path):
    ocr = CnOcr()
    return ocr.ocr(path)


def ocr_v3(img_path):
    # orc = CnOcr(rec_model_name=det_model_name)
    orc = CnOcr(rec_model_name='ch_PP-OCRv3')
    return orc.ocr(img_path)


def ocr_txt_v3(img_path):
    return ocr_v3(img_path)


def ocr_txt_zhengbing(img_path, auto_txt, area=(0, 0, 0, 0)):
    general_screenshot_tools(area)
    if reg_list_name(ocr_default(img_path))[0] != auto_txt:
        return False
    else:
        return True


def ocr_txt_click(img_path, auto_text, model='', area=(), isADDWH=False):
    d = return_device()
    if model == 'ch_PP-OCRv3':
        ocr = CnOcr(rec_model_name=model)
    elif model == 'naive_det':
        ocr = CnOcr(det_model_name=model)
    else:
        ocr = CnOcr()
    if area and len(area) == 4:
        Image.open(img_path).crop(area).save(img_path)
        out = ocr.ocr(img_path)
    else:
        out = ocr.ocr(img_path)
    for v in out:
        print(v)
        if v['text'] == auto_text:
            x, y = reg_coor(v['position'])
            if isADDWH:
                x += area[0]
                y += area[1]
            print(x, y)
            d.click(x, y)
            return True
    return False

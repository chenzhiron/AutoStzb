from path.img import path
from ocr.main import ocr_txt_zhengbing
w = 742
h = 500
w2 = 863
h2 = 670


def module_zhengbing_click(device):
    device.screenshot().crop((w, h, w2, h2)).save(path)
    if ocr_txt_zhengbing(path, (w,h,w2,h2), '证兵'):
        device.click( (w + w2) /2, (h+h2) / 2)
        return True
    else:
        return False


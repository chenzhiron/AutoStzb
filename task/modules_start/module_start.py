from ocr.main import ocr_txt_click
from device.main import return_device

def module_click_start(path, auto_text):
    d = return_device()
    d.screenshot().save(path)
    return ocr_txt_click(path, auto_text)

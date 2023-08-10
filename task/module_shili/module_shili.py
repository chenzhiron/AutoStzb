from device.main import return_device
from ocr.main import ocr_txt_click
from task.module_shili.address_area import area
from ocr.ocr_model_name import vertical_model_name


def module_click_shili(path, auto_text):
    d = return_device()
    d.screenshot().save(path)
    result = ocr_txt_click(path, auto_text, vertical_model_name, area, True)
    return result

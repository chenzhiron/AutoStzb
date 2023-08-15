from ocr.main import ocr_txt_click, ocr_txt
from ocr.ocr_model_name import vertical_model_name
from task.module_duiwu.address_area import list_name_area, list_click_area
from tools.reg_list_name import reg_list_name

def module_ocr_duiwu_name(device, path, is_main=False):
    area = list_name_area,
    if is_main:
        area = list_click_area
    device.screenshot().crop(area).save(path)
    result = ocr_txt(path)
    return reg_list_name(result)


def module_click_duiwu(device, path, auto_txt, is_main=False):
    area = list_name_area
    if is_main:
        area = list_click_area
    device.screenshot().save(path)
    return ocr_txt_click(path, auto_txt, vertical_model_name, area, True)


if __name__ == '__main__':
    from path.img import path
    res = ocr_txt(path)
    print(res)
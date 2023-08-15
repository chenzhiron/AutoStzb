from ocr.main import ocr_txt_click, ocr_txt
from ocr.ocr_model_name import vertical_model_name
from tools.reg_list_name import reg_list_name
from path.img import path
from PIL import Image


def module_ocr_duiwu_name(path, is_main=False):
    result = ocr_txt(path)
    return reg_list_name(result)


if __name__ == '__main__':
    img = Image.open(path)
    width, height = img.size
    img.resize((width * 3, height * 3)).save('./demo.jpg')

    res = module_ocr_duiwu_name(path, True)
    print(res)

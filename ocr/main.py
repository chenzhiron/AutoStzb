from pix2text import Pix2Text

from tools.reg_screenshot import general_screenshot_tools


def ocr_default(path):
    p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
    ocr = p2t.recognize(path, resized_shape=608, use_analyzer=False)
    print(ocr)
    if ocr:
        return ocr[0]['text']
    else:
        return []


def ocr_txt_verify(path, auto_txt, area=(0, 0, 0, 0)):
    general_screenshot_tools(area)
    result = ocr_default(path)
    print(result + auto_txt)
    if result:
        if str(result) != str(auto_txt):
            return False
        else:
            print('True:::')
            return True
    else:
        return False

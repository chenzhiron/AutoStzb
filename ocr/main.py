
from paddleocr import PaddleOCR
# from tools.reg_screenshot import general_screenshot_tools


def ocr_default(paths):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    result = ocr.ocr(paths, cls=True)
    return result
    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)
    # p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
    # ocr = p2t.recognize(path, resized_shape=608, use_analyzer=False)
    # print(ocr)
    # if ocr:
    #     return ocr[0]['text']
    # else:
    #     return []


def ocr_txt_verify(path, auto_txt, area=(0, 0, 0, 0)):
    # general_screenshot_tools(area)
    # result = ocr_default(path)
    # print(result + auto_txt)
    # if result:
    #     if str(result) != str(auto_txt):
    #         return False
    #     else:
    #         print('True:::')
    #         return True
    # else:
        return False
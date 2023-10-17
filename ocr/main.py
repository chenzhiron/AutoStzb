from paddleocr import PaddleOCR

from device.main_device import return_device
import numpy as np


# from tools.reg_screenshot import general_screenshot_tools


def ocr_default(sources):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    result = ocr.ocr(sources, cls=False)
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


def ocr_txt_verify(area=(0, 0, 0, 0)):
    device = return_device()
    img_sources = device.screenshot().crop(area)
    result = ocr_default(np.array(img_sources))
    if bool(result[0]):
        return [item[1][0] for sublist in result for item in sublist]
    else:
        return None


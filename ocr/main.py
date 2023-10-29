from paddleocr import PaddleOCR

from device.automation import get_screenshot

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory


def ocr_default(sources):
    result = ocr.ocr(sources, cls=False)
    print(result)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)


def ocr_txt_verify(area=(0, 0, 0, 0)):
    result = ocr_default(get_screenshot(area))
    if bool(result[0]):
        return [item[1][0] for sublist in result for item in sublist]
    else:
        return None


from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory


def ocr_default(sources):
    result = ocr.ocr(sources, cls=False)
    print(result)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)


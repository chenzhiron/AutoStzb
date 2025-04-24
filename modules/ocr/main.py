import numpy as np
from paddleocr import PaddleOCR

from modules.devices.main import Devices

ocr = PaddleOCR(
    lang="ch",
    show_log=True,
)


def ocrnotdet(sources):
    return ocr.ocr(sources, cls=False, det=False, inv=True)


def ocrnormal(sources):
    return ocr.ocr(sources, cls=False, inv=True)

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)


def ocr_format_ranking(sources):
    data = ocrnormal(sources)
    if data[0] is None:
        return None

    result = []

    for v in data[0]:
        t = v[0][0][1]
        b = v[0][2][1]
        name = v[1][0]
        print("t,b,n:", t, b, name)
        result.append([t, b, name])

    return result


def ocr_format_val(sources):
    v = ocrnormal(sources)
    if v[0] is None:
        return None
    try:
        result = ""
        for outer_list in v:
            for inner_list in outer_list:
                for element in inner_list:
                    if isinstance(element, tuple):
                        result += element[0]
        print(result)
        return result
    except:
        return None


if __name__ == '__main__':
    d = Devices('127.0.0.1:16384')
    result = ocrnormal(np.array(d.screenshot()))
    print(result)

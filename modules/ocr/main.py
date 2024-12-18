# from config.config import globalConfig
from paddleocr import PaddleOCR

import os

ocr_det = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "models", "ch_PP-OCRv4_det_infer.infer"
)
ocr_rec = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "models", "ch_PP-OCRv4_rec_infer.infer"
)
ocr_cls = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "models",
    "ch_ppocr_mobile_v2.0_cls.infer",
)
ocr_keys = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "models", "ppocr_keys_v1.txt"
)

# ocr_det = globalConfig['Ocr']['det']
# ocr_rec = globalConfig['Ocr']['rec']
# ocr_cls = globalConfig['Ocr']['cls']
# ocr_keys = globalConfig['Ocr']['keys']
ocr = PaddleOCR(
    lang="ch",
    # det_model_dir=ocr_det,
    # rec_model_dir=ocr_rec,
    # cls_model_dir=ocr_cls,
    # rec_char_dict_path=ocr_keys,
    show_log=True,
    savefile=True
)

def ocrnotdet(sources):
    result = ocr.ocr(sources, cls=False, det=False, inv=True)
    return result

def ocrnormal(sources):
    result = ocr.ocr(sources, cls=False, inv=True)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)


def ocr_format_ranking(sources):
    data = ocrnormal(sources)
    if data[0] == None:
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
    if v[0] == None:
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

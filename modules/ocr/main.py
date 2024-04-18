# from config.config import globalConfig
from paddleocr import PaddleOCR

import os

ocr_det = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'ch_PP-OCRv4_det_infer.infer')
ocr_rec = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'ch_PP-OCRv4_rec_infer.infer')
ocr_cls = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'ch_ppocr_mobile_v2.0_cls.infer')
ocr_keys = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'ppocr_keys_v1.txt')

# ocr_det = globalConfig['Ocr']['det']
# ocr_rec = globalConfig['Ocr']['rec']
# ocr_cls = globalConfig['Ocr']['cls']
# ocr_keys = globalConfig['Ocr']['keys']
ocr = PaddleOCR(lang="ch",
                det_model_dir=ocr_det,
                rec_model_dir=ocr_rec,
                cls_model_dir=ocr_cls,
                rec_char_dict_path=ocr_keys,
                show_log=False,
                )


def ocrDefault(sources):
    result = ocr.ocr(sources, cls=False)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)

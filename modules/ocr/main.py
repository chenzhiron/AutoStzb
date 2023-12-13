from config.paths import ocr_det, ocr_rec, ocr_cls, ocr_keys
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="ch",
                det_model_dir=ocr_det,
                rec_model_dir=ocr_rec,
                cls_model_dir=ocr_cls,
                rec_char_dict_path=ocr_keys,
                use_gpu=False,
                show_log=False
                )


def ocrDefault(sources):
    result = ocr.ocr(sources, cls=False)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)

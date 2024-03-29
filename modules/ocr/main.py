from config.config import globalConfig
from paddleocr import PaddleOCR

ocr_det = globalConfig['Ocr']['det']
ocr_rec = globalConfig['Ocr']['rec']
ocr_cls = globalConfig['Ocr']['cls']
ocr_keys = globalConfig['Ocr']['keys']
ocr = PaddleOCR(lang="ch",
                det_model_dir=ocr_det,
                rec_model_dir=ocr_rec,
                cls_model_dir=ocr_cls,
                rec_char_dict_path=ocr_keys,
                show_log=True,
                save_crop_res=True,
                warmup=True
                )


def ocrDefault(sources):
    result = ocr.ocr(sources, cls=False)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)

from paddleocr import PaddleOCR
import os

current_directory = os.getcwd()
del_model = os.path.join(current_directory, "ocr", "ch_PP-OCRv4_det_infer")
rec_model = os.path.join(current_directory, "ocr", "ch_PP-OCRv4_rec_infer")
cls_model = os.path.join(current_directory, "ocr", "ch_ppocr_mobile_v2.0_cls_infer")
rec_char_dict = os.path.join(current_directory, "ocr", 'ppocr_keys_v1.txt')
ocr = PaddleOCR(lang="ch",
                det_model_dir=del_model,
                rec_model_dir=rec_model,
                cls_model_dir=cls_model,
                rec_char_dict_path=rec_char_dict,
                use_gpu=False
                )


def ocrDefault(sources):
    result = ocr.ocr(sources, cls=False)
    print(result)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)

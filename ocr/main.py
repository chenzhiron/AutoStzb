from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="ch",
                det_model_dir="./ch_PP-OCRv4_det_infer",
                rec_model_dir="./ch_PP-OCRv4_rec_infer",
                cls_model_dir="./ch_ppocr_mobile_v2.0_cls_infer",
                )


def ocr_default(sources):
    result = ocr.ocr(sources, cls=False)
    print(result)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)

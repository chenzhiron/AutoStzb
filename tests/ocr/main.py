from config.config import globalConfig
from paddleocr import PaddleOCR

ocr_det = globalConfig['Ocr']['det']
ocr_rec = globalConfig['Ocr']['rec']
ocr_cls = globalConfig['Ocr']['cls']
ocr_keys = globalConfig['Ocr']['keys']
# ocr = PaddleOCR(lang="ch",
#                 det_model_dir=ocr_det,
#                 rec_model_dir=ocr_rec,
#                 cls_model_dir=ocr_cls,
#                 rec_char_dict_path=ocr_keys,
#                 save_crop_res=True,
#                 use_space_char=False,
#                 use_angle_cls=True,
#                 对出征编队处编号格式化
#                 det_db_unclip_ratio=10
#                 )

ocr = PaddleOCR(lang="ch",
                det_model_dir=ocr_det,
                rec_model_dir=ocr_rec,
                cls_model_dir=ocr_cls,
                rec_char_dict_path=ocr_keys,
                save_crop_res=True,
                use_space_char=False,
                use_dilation=True,
                # use_angle_cls=True,
                det_db_score_mode="slow",
                det_db_unclip_ratio=10,
                det_db_box_thresh=0.1,
                det_db_thresh=0.1,
                max_batch_size=1
                )


def ocrDefault(sources):
    result = ocr.ocr(sources, cls=False)
    return result

    # for idx in range(len(result)):
    #     res = result[idx]
    #     for line in res:
    #         print(line)

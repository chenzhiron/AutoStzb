import os

# # 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取当前项目的路径
project_dir = os.path.dirname(current_dir)
adb = os.path.join(project_dir, 'device', 'adb', 'adb.exe').replace('\\', '/')
ocr_det = os.path.join(project_dir, 'modules', 'ocr', 'ch_PP-OCRv4_det_infer').replace('\\', '/')
ocr_rec = os.path.join(project_dir, 'modules', 'ocr', 'ch_PP-OCRv4_rec_infer').replace('\\', '/')
ocr_cls = os.path.join(project_dir, 'modules', 'ocr', 'ch_ppocr_mobile_v2.0_cls_infer').replace('\\', '/')
ocr_keys = os.path.join(project_dir, 'modules', 'ocr', 'ppocr_keys_v1.txt').replace('\\', '/')

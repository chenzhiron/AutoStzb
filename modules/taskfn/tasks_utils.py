import cv2
import numpy as np
from modules.ocr.main import ocr_format_val
from modules.utils import formatDate


def battle_time(img, v):
    # 战报时间
    times = formatDate(
        ocr_format_val(np.array(img.crop([665, v + 240, 900, v + 240 + 40])))
    ) or formatDate(
        ocr_format_val(np.array(img.crop([665, v + 230, 900, v + 230 + 50])))
    )
    if type(times) is str or times is None:
        times = formatDate(
            ocr_format_val(
                np.array(img.crop([665, v + 230 + 80, 900, v + 230 + 80 + 60]))
            )
        )
    print("times", times)
    return times


class BaseTypeImg:
    def __init__(self):
        self.attack_template_img = cv2.imread(
            "./modules/imgs/attack_template.png", cv2.IMREAD_COLOR
        )
        self.defense_template_img = cv2.imread(
            "./modules/imgs/defense_template.png", cv2.IMREAD_COLOR
        )
        self.exploit_template_img = cv2.imread(
            "./modules/imgs/condinate.png", cv2.IMREAD_COLOR
        )

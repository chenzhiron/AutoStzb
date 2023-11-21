import numpy as np

from device.AutoMation import automation
from device.operate import operateTap
from modules.general.option_verify_area import tili_area, address_execute_list, status_area, person_status_number_area, \
    enemy_status_number_area, computed_going_list_area, bianduilists
from modules.utils.main import ocr_reg, calculate_max_timestamp
from ocr.main import ocrDefault


# 选择对应的部队出征
def select_active_lists(l, area=bianduilists):
    image = automation.getScreenshots()
    content = ocrDefault(np.array(image.crop(area)))
    result = ocr_reg(content)
    if len(result) > 0:
        try:
            current_max = int(result[0][2]) - 1
        except:
            return False
        residue_tili = ocr_reg(ocrDefault(np.array(image.crop(tili_area[current_max][l - 1]))))
        if len(residue_tili) > 0 and residue_tili[0] is not None:
            return calculate_max_timestamp(residue_tili)
        else:
            x, y = address_execute_list[current_max][l - 1]
            operateTap(x, y)
            return True
    else:
        return False


# 战报详情数据
def battle_info():
    image = automation.getScreenshots()
    battle_result = {'status': ocr_reg(ocrDefault(np.array(image.crop(status_area))))[0],
                     'person_number': ocr_reg(ocrDefault(np.array(image.crop(person_status_number_area))))[0],
                     'enemy_number': ocr_reg(ocrDefault(np.array(image.crop(enemy_status_number_area))))[0]}
    return battle_result

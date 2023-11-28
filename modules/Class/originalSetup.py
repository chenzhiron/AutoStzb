from modules.Class.OperatorSteps import OriginalOperatorSteps, OperatorSteps
from modules.general.module_options_name import saodang
from modules.general.option_verify_area import address_execute_order_area, zhengbing_time_area, computed_going_time_area
from modules.utils import calculate_max_timestamp, ocr_reg

# 点击扫荡 / 点击出征
click_options_options = OriginalOperatorSteps(address_execute_order_area, saodang, 820, 200)

# 识别征兵时间
zhengbing_ocr_max = OperatorSteps(zhengbing_time_area, None)
# 识别出征时间
chuzheng_ocr_max = OperatorSteps(computed_going_time_area, None)


# 征兵时间
def zhengbing_max_time():
    result = zhengbing_ocr_max.getImgOcr()
    max_time = calculate_max_timestamp(ocr_reg(result))
    return max_time


# 出征时间
def chuzheng_max_time():
    result = chuzheng_ocr_max.getImgOcr()
    max_time = calculate_max_timestamp(ocr_reg(result))
    return max_time

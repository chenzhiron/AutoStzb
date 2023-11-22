from modules.Class.OperatorSteps import OriginalOperatorSteps, OperatorSteps
from modules.general.module_options_name import saodang, chuzheng
from modules.general.option_verify_area import address_execute_order_area, zhengbing_time_area, computed_going_time_area
from modules.utils.main import calculate_max_timestamp, ocr_reg

# 点击扫荡 / 点击出征
click_options_options = OriginalOperatorSteps(address_execute_order_area, saodang, 820, 200)


# 识别时间
def ocr_max_time(area):
    obj = OperatorSteps(area, None)
    result = obj.getImgOcr()
    max_time = calculate_max_timestamp(ocr_reg(result))
    return max_time


# 征兵时间
def zhengbing_max_time():
    return ocr_max_time(zhengbing_time_area)


# 出征时间
def chuzheng_max_time():
    return ocr_max_time(computed_going_time_area)

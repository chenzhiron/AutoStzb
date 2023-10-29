import time

from device.operate import operate_adb_tap
from device.automation import get_screenshot
from modules.general.generalExecuteFn import calculate_max_timestamp, reg_ocr_verify, executeFn
from modules.module_address.module_address_area import address_sign_area, \
    address_area_start, address_sign_land_area, address_execute_order_area, \
    address_execute_list, computed_going_time_area, address_sign_verify, computed_going_list

from ocr.main import ocr_txt_verify, ocr_default

from modules.general.module_options_name import saodang, going_list_txt


# 点击标记选项
def module_address_start():
    ocr_txt = ocr_txt_verify(address_sign_verify)
    if ocr_txt is None:
        operate_adb_tap(address_area_start[0], address_area_start[1])


# 点击区域
def module_sign_area_area_click():
    executeFn(reg_ocr_verify(address_sign_verify, 2), '标记')
    operate_adb_tap(address_sign_area[0], address_sign_area[1])


# 点击标记的土地
def module_sign_land_area_click():
    count = 0
    while count < 12:
        result = ocr_txt_verify(address_sign_land_area)
        if bool(result):
            operate_adb_tap(address_sign_land_area[0], address_sign_land_area[1])
            break
        else:
            count += 1
            if count == 12:
                raise ZeroDivisionError("点击土地识别出错了")


# 选择扫荡/出征
def module_sign_Execute_order(autotxt='扫荡'):
    time.sleep(3)
    count = 0
    while count < 12:
        result = ocr_default(get_screenshot(address_execute_order_area))
        # 选择扫荡
        if bool(result):
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    if line[1][0] == autotxt:
                        first_list = line[0]
                        center_point = [sum(coord) / len(coord) for coord in zip(*first_list)]
                        time.sleep(0.3)
                        operate_adb_tap(820 + center_point[0], 250 + center_point[1])
                        print(line)
                        break
                break
            break
        else:
            count += 1
            if count == 12:
                raise ZeroDivisionError("点击土地识别出错了")


# 选择出征队伍，需要计算传入的值
def module_execute_list_click(i):
    # 选择出征队伍页面校验
    executeFn(reg_ocr_verify(computed_going_list, 5), going_list_txt)
    x, y = address_execute_list
    # 此处需要计算还有重试
    operate_adb_tap(x, y)
    # ocr_txt = ocr_txt_verify((820, 250, 1150, 510))
    # print(ocr_txt)


# 计算出征时间
def module_computed_going_time():
    ocr_txt = ocr_txt_verify(computed_going_time_area)
    result = calculate_max_timestamp(ocr_txt)
    print(result)
    return result


# 点击扫荡
def executed_going_list():
    # result = executeFn(
    #     reg_ocr_verify(
    #         (1082, 640, 1150, 680),
    #         2
    #     ),
    #     saodang
    # )
    operate_adb_tap(1020, 660)

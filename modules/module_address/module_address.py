from device.main import adb_tap, get_screenshot
from modules.general.generalExecuteFn import calculate_max_timestamp, reg_ocr_verify, executeFn
from modules.module_address.module_address_area import address_sign_area, \
    address_area_start, address_sign_land_area, address_execute_order_area, \
    address_execute_list, computed_going_time_area, address_sign_verify

from ocr.main import ocr_txt_verify

from modules.general.module_options_name import saodang


# 点击标记选项
def module_address_start():
    ocr_txt = ocr_txt_verify(address_sign_verify)
    if ocr_txt is None:
        adb_tap(address_area_start[0], address_area_start[1])


# 点击区域
def module_sign_area_area_click():
    adb_tap(address_sign_area[0], address_sign_area[1])


# 点击标记的土地
def module_sign_land_area_click():
    adb_tap(address_sign_land_area[0], address_sign_land_area[1])


# 选择扫荡/出征
def module_sign_Execute_order(autotxt='扫荡'):
    from ocr.main import ocr_default
    result = ocr_default(get_screenshot(address_execute_order_area))
    # 选择扫荡
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            if line[1][0] == autotxt:
                first_list = line[0]
                center_point = [sum(coord) / len(coord) for coord in zip(*first_list)]
                adb_tap(820 + center_point[0], 250 + center_point[1])
                print(line)
                break


# 选择出征队伍，需要计算传入的值
def module_execute_list_click(i):
    adb_tap(address_execute_list[0], address_execute_list[1])
    ocr_txt = ocr_txt_verify((820, 250, 1150, 510))
    print(ocr_txt)


# 计算出征时间
def module_computed_going_time():
    ocr_txt = ocr_txt_verify(computed_going_time_area)
    result = calculate_max_timestamp(ocr_txt)
    print(result)


# 点击扫荡
def executed_going_list():
    result = executeFn(
        reg_ocr_verify(
            (1082, 640, 1150, 680),
            2
        ),
        saodang
    )
    print(result)

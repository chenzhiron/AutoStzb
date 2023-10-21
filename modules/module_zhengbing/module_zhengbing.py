from device.main import adb_tap, adb_swipe
from modules.general.generalExecuteFn import executeFn, reg_ocr_verify, executeClickArea, calculate_max_timestamp
from modules.general.module_options_name import zhengbing, require_zhengbing, shili, queding
from modules.module_zhengbing.module_zhengbing_area import (zhengbing_page_area,
                                                            zhengbing_page_swipe,
                                                            zhengbing_time_area,
                                                            zhengbing_page_verify_area,
                                                            zhengbing_page_swipe_verify, zhengbing_require_click,
                                                            zhengbing_next_click, return_page_area,
                                                            return_page_next_area, queding_area, click_list_x_y,
                                                            )
from ocr.main import ocr_txt_verify


# 势力页面点击队伍征兵选项
def module_zhengbing_list_click(i):
    executeFn(reg_ocr_verify(zhengbing_page_verify_area, 2), shili)
    x, y = click_list_x_y
    adb_tap(x * i, y)


# 点击征兵按钮
def module_zhengbing_page_click():
    executeFn(reg_ocr_verify(zhengbing_page_area, 2), zhengbing)
    x,y = executeClickArea(zhengbing_page_area)
    adb_tap(x, y)


# 校验是否进入并滑动
def module_swipe_zhengbing_page():
    executeFn(reg_ocr_verify(zhengbing_page_swipe_verify, 4), require_zhengbing)
    for v in zhengbing_page_swipe:
        adb_swipe(v[0], v[1], v[2], v[3])


# 计算征兵时间
def module_computed_time():
    result = ocr_txt_verify(zhengbing_time_area)
    times = calculate_max_timestamp(result)
    print(times)
    return times


# 确认征兵
def module_require_zhengbing():
    adb_tap(zhengbing_require_click[0], zhengbing_require_click[1])


# 再次确认
def module_require_next_click():
    executeFn(reg_ocr_verify(queding_area, 2), queding)
    adb_tap(zhengbing_next_click[0], zhengbing_next_click[1])


# 二级返回
def module_return_page():
    adb_tap(return_page_area[0], return_page_area[1])


# 一级返回
def module_return_next_page():
    # 识别x
    adb_tap(return_page_next_area[0], return_page_next_area[1])

# 验证征兵已满
# def module_verify_zhengbing():
#     time_number = 5
#     while time_number > 0:
#         time.sleep(TIMESLEEP)
#         if ocr_txt_verify(path, zhengbing_verify, zhengbing_page_queren_area):
#             return True
#         time_number -= 1
#     return False

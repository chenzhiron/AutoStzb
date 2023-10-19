from device.main import adb_tap, adb_swipe
from modules.general.generalExecuteFn import executeFn, reg_ocr_verify, executeClickArea, calculate_max_timestamp
from modules.general.module_options_name import zhengbing, require_zhengbing, shili
from modules.module_zhengbing.module_zhengbing_area import (zhengbing_page_area,
                                                            zhengbing_page_swipe,
                                                            zhengbing_time_area,
                                                            zhengbing_page_verify_area,
                                                            zhengbing_page_swipe_verify, zhengbing_require_click,
                                                            zhengbing_next_click, return_page_area,
                                                            return_page_next_area,
                                                            )





# 势力页面点击队伍征兵选项
def module_zhengbing_list_click(i):
    result = executeFn(reg_ocr_verify(zhengbing_page_verify_area, 2), shili)
    if result:
        # adb_tap(100, 260)
        # 此处需要计算各队伍坐标
        adb_tap(100, 260)


# 点击征兵按钮
def module_zhengbing_page_click():
    result = executeFn(reg_ocr_verify(zhengbing_page_area, 2), zhengbing)
    if result:
        adb_tap(executeClickArea(zhengbing_page_area)[0], executeClickArea(zhengbing_page_area)[1])


# 校验是否进入并滑动
def module_swipe_zhengbing_page():
    result = executeFn(reg_ocr_verify(zhengbing_page_swipe_verify, 4), require_zhengbing)
    if result:
        for v in zhengbing_page_swipe:
            adb_swipe(sx=v[0], sy=v[1], ex=v[2], ey=v[3])


# 计算征兵时间
def module_computed_time():
    result = reg_ocr_verify(zhengbing_time_area, 999)()
    times = calculate_max_timestamp(result)
    print(times)
    return times


# 确认征兵
def module_require_zhengbing():
    adb_tap(zhengbing_require_click[0], zhengbing_require_click[1])


# 再次确认
def module_require_next_click():
    adb_tap(zhengbing_next_click[0], zhengbing_next_click[1])


# 二级返回
def module_return_page():
    adb_tap(return_page_area[0], return_page_area[1])


# 一级返回
def module_return_next_page():
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

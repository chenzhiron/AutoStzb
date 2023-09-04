from device.main_device import return_device
from modules.module_address.module_address_area import address_affirm_button
from modules.module_zhengbing.module_zhengbing_area import (zhengbing_page_area,
                                                            zhengbing_page_swipe,
                                                            zhengbing_page_queren_area,
                                                            zhengbing_time_area,
                                                            zhengbing_time_queren_area,
                                                            )
from ocr.main import ocr_txt_verify, ocr_default
from tools.reg_click_direction import reg_direction
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_time import split_string, reg_time


# 进入点击征兵页面
def module_zhengbing_click(img_path, auto_txt='证兵'):
    time_number = 0
    while 1:
        if ocr_txt_verify(img_path, auto_txt, zhengbing_page_area):
            device = return_device()
            x, y = reg_direction(zhengbing_page_area)
            device.click(x, y)
            return True
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('点击征兵，进入征兵进度条失败')


# 滑动征兵模块
def module_swipe_zhengbing_click(img_path, auto_txt='确认证兵'):
    time_number = 0
    while 1:
        if ocr_txt_verify(img_path, auto_txt, zhengbing_page_queren_area):
            for v in zhengbing_page_swipe:
                device = return_device()
                device.swipe(sx=v[0], sy=v[1], ex=v[2], ey=v[3], duration=v[4])
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('拖动征兵进度条失败')


# 计算征兵时间
def module_zhengbing_computed_time(img_path):
    general_screenshot_tools(zhengbing_time_area)
    result = ocr_default(img_path).replace('\n', '').replace('\r', '')
    result = split_string(result, 8)
    max_time = []
    for v in result:
        max_time.append(reg_time(v))
    max_time.sort(reverse=True)
    return max_time[0]
    # 后续逻辑


# 点击确认征兵按钮
def module_zhengbing_affirm_btn():
    device = return_device()
    x, y = address_affirm_button
    device.click(x, y)


# 确定征兵
def module_zhuangbing_require(img_path, auto_txt='确定'):
    time_number = 0
    while 1:
        # 确认 区域重新点击
        if ocr_txt_verify(img_path, auto_txt, zhengbing_time_queren_area):
            device = return_device()
            x, y = reg_direction(zhengbing_time_queren_area)
            device.click(x, y)
            break
        else:
            time_number += 1
        if time_number == 50:
            raise Exception('征兵确认时间点击错误')

# if __name__ == '__main__':
#     connect_device()
#     module_zhengbing_click(path)
#     module_swipe_zhengbing_click(path)
#     maxtime = module_zhengbing_computed_time(path)
#     print(maxtime)
#     module_zhengbing_affirm_btn()
#     module_zhuangbing_require(path)

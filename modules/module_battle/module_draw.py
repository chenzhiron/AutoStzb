from device.main_device import return_device
from modules.general.module_options_name import person_battle
from config.img import path
from module_draw_area import battlefield, person_battle_area, person_status_number_area, enemy_status_number_area, \
    status_area, click_battle, discern_time_area
from ocr.main import ocr_txt_verify, ocr_default
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_time import reg_time


# 点击战报 对比时间 误差3s  查看平局 / 胜利 / 失败 ，截图
def module_computed_draw(times, offset=3):
    device = return_device()
    data_dist = {
        "blue": 4500,
        "red": 3400,
        "result": "",
    }
    # 识别战报时间，对比队伍出征时间，最大误差3s(涉及到下滑战报问题)
    general_screenshot_tools(discern_time_area)
    exact_time = ocr_default(path)
    exact_time = reg_time(exact_time)
    residue_time = exact_time - times
    if residue_time > offset:
        pass

    x, y = battlefield
    device.click(x, y)
    if ocr_txt_verify(path, person_battle, person_battle_area):
        general_screenshot_tools(status_area)
        result = ocr_default(path)

        if result == '成功':
            data_dist["result"] = "success"
        elif result == '失败':
            data_dist["result"] = "lose"
        elif result == '平局':
            data_dist["result"] = "deuce"

        data_dist["result"] = result
    x2, y2 = click_battle
    device.click(x2, y2)
    general_screenshot_tools(person_status_number_area)
    # 数值处理
    person_number = ocr_default(path)
    general_screenshot_tools(enemy_status_number_area)
    # 数值处理
    enemy_number = ocr_default(path)

    data_dist["blue"] = int(person_number)
    data_dist["red"] = int(enemy_number)

    return data_dist

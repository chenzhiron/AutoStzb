import time

import datetime

from config.paths import path

from modules.general.module_options_name import person_battle, battle_details
from modules.module_battle.module_draw_area import battlefield, person_battle_area, person_status_number_area, \
    enemy_status_number_area, \
    status_area, click_battle
from modules.module_fanhui.module_fanhui import module_return_index
from ocr.main import ocr_txt_verify, ocr_default
from tools.reg_screenshot import general_screenshot_tools


# 点击战报 对比时间 误差3s  查看平局 / 胜利 / 失败 ，截图
def module_computed_draw(going_list, times):
    from device.main_device import return_device
    start_time = time.time()
    time_number = 50
    device = return_device()
    data_dist = {
        "blue": 0,
        "red": 0,
        "result": "",
        "times": 0,
        "timed": 0,
        'lists': going_list
    }
    x, y = battlefield
    device.click(x, y)
    while time_number > 0:
        if ocr_txt_verify(path, person_battle, person_battle_area):
            general_screenshot_tools(status_area)
            battle_result = ocr_default(path)
            if battle_result == '胜利':
                battle_success(data_dist, start_time)
            elif battle_result == '战败':
                battle_lose(data_dist, start_time)
            elif battle_result == '平局':
                battle_deuce(data_dist, start_time)
            else:
                pass
            module_return_index()
            module_return_index()
            module_return_index()
            module_return_index()
            data_dist['times'] = times - data_dist['times'] if times - data_dist['times'] > 0 else 0
            return data_dist
        else:
            time_number -= 1
    return False


def battle_success(data_dist, start_time):
    data_dist["result"] = "success"
    end_time = time.time()
    data_dist["times"] = int(end_time - start_time)
    data_dist['timed'] = data_dist['times']
    return data_dist


def battle_lose(data_dist, start_time):
    data_dist["result"] = "lose"
    end_time = time.time()
    data_dist["times"] = int(end_time - start_time)
    data_dist['timed'] = data_dist['times']
    return data_dist


def battle_deuce(data_dist, start_time):
    from device.main_device import return_device
    time_number = 50
    device = return_device()
    data_dist["result"] = "deuce"
    x2, y2 = click_battle
    device.click(x2, y2)
    while time_number > 0:
        if ocr_txt_verify(path, battle_details, person_battle_area):
            general_screenshot_tools(person_status_number_area)
            person_number = ocr_default(path)
            general_screenshot_tools(enemy_status_number_area)
            enemy_number = ocr_default(path)
            data_dist["blue"] = int(person_number.split('/')[0])
            data_dist["red"] = int(enemy_number.split('/')[0])
            end_time = time.time()
            data_dist["times"] = int(end_time - start_time)
            data_dist['timed'] = data_dist['times']
            return data_dist
        else:
            time_number -= 1
    return False

# if __name__ == '__main__':
#     connect_device()
# result = module_computed_draw(16913928710, 1)
# result = battle_success({"blue": 0, "red": 0, "result": "", "task_id": 1, "times": 0}, 0)
# print(str(result))
# module_return_index()
# time.sleep(0.5)
# module_return_index()

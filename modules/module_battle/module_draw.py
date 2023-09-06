from device.main_device import return_device, connect_device
from modules.general.module_options_name import person_battle, battle_details
from config.img import path
from module_draw_area import battlefield, person_battle_area, person_status_number_area, enemy_status_number_area, \
    status_area, click_battle, discern_time_area
from ocr.main import ocr_txt_verify, ocr_default
from tools.reg_screenshot import general_screenshot_tools
from tools.reg_time import reg_time, reg_time_ymd


# 点击战报 对比时间 误差3s  查看平局 / 胜利 / 失败 ，截图
def module_computed_draw(times, offset=3):
    time_number = 50
    device = return_device()
    data_dist = {
        "blue": 0,
        "red": 0,
        "result": "",
    }
    x, y = battlefield
    device.click(x, y)
    while time_number > 0:
        if ocr_txt_verify(path, person_battle, person_battle_area):
            # 识别战报时间，对比队伍出征时间，最大误差3s(涉及到下滑战报问题)
            general_screenshot_tools(discern_time_area)
            exact_time = ocr_default(path)
            exact_time = reg_time_ymd(exact_time)
            residue_time = exact_time - times
            if residue_time <= offset:
                general_screenshot_tools(status_area)
                battle_result = ocr_default(path)
                if battle_result == '胜利':
                    data_dist["result"] = "success"
                    return data_dist
                elif battle_result == '战败':
                    data_dist["result"] = "lose"
                    return data_dist
                elif battle_result == '平局':
                    data_dist["result"] = "deuce"
                x2, y2 = click_battle
                device.click(x2, y2)
                while time_number > 0:
                    print(battle_details)
                    if ocr_txt_verify(path, battle_details, person_battle_area):
                        general_screenshot_tools(person_status_number_area)
                        person_number = ocr_default(path)
                        general_screenshot_tools(enemy_status_number_area)
                        enemy_number = ocr_default(path)
                        data_dist["blue"] = int(person_number.split('/')[0])
                        data_dist["red"] = int(enemy_number.split('/')[0])
                        return data_dist
                    else:
                        time_number -= 1
        else:
            time_number -= 1
    return data_dist


# if __name__ == '__main__':
#     connect_device()
#     result = module_computed_draw(16913928710)
#     print(str(result))

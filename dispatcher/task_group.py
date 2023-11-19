from modules.pageSwitch.page_switch import *

# 征兵
conscription = [handle_in_map_conscription]
# 扫荡
mopping_up_fast = [handle_in_lists_action, handle_in_battle_result]
mopping_up = [handle_in_lists_action, handle_in_battle_result, handle_in_map_conscription]
# 出征
conquer = [handle_sign_action, handle_in_lists_action, handle_in_battle_result, handle_in_map_conscription,
           handle_unmark]

task_all = {}


def set_task_all(key, value):
    task_all[key] = value


def get_task_all(key):
    return task_all[key]


def clear_task_all(key):
    task_all[key] = []

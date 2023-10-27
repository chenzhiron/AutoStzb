from modules.tasks.battle import battle
from modules.tasks.saodang import saodang
from modules.tasks.zhengbing import zhengbing

# 征兵
conscription = [zhengbing]
# 扫荡
mopping_up = [saodang, battle, zhengbing]
# 出征


task_all = {}


def set_task_all(key, value):
    task_all[key] = value


def get_task_all(key):

    return task_all[key]


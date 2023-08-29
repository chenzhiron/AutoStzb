from tasks.saodang import saodang
from tasks.zhengbing import zhengbing


def execute_tasks(task_list):
    if task_list[0] == 1:
        zhengbing(task_list[1])
    if task_list[0] == 2:
        saodang(task_list[1])
        # zhengbing(task_list[1])




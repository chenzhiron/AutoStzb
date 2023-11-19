import copy

from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

from dispatcher.status import result_queue
from dispatcher.task_group import get_task_all, set_task_all
from modules.pageSwitch.page_switch import handle_in_lists_action, handle_battle_draw_result
from modules.taskConfigStorage.main import get_config_storage_by_key
from modules.utils.main import get_current_date

# 创建调度器
scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)},
                                job_defaults={'misfire_grace_time': 10})


def start_scheduler():
    scheduler.start()
    scheduler.add_listener(job_executed, EVENT_JOB_EXECUTED)


# 在此处任务进行校验跟添加任务
def job_executed(event):
    object_dict = vars(event)
    task_id = object_dict['job_id']
    task_next_fn = get_task_all(task_id)
    current_config_storage = get_config_storage_by_key(task_id)
    print('job_executed', task_id, task_next_fn)
    print('current_config_storage', current_config_storage)
    if len(task_next_fn) > 0:
        # 1.扫荡 -> 2.查看战报 -> 3.胜利-失败/平局

        # 出发/扫荡
        if current_config_storage['type'] == 2:
            seconds = current_config_storage['times']
            next_fn = task_next_fn.pop(0)
            # 如果没有体力 进行等待 再进行出发
            if current_config_storage['result'] is not None:
                next_fn = handle_in_lists_action
                seconds = current_config_storage['result']
            # 等待执行下一步任务
            sc_cron_add_jobs(next_fn, [task_id], task_id, seconds)
        # 战报结果
        elif current_config_storage['type'] == 3:
            if current_config_storage['battle_result']['status'] == '胜利' or current_config_storage['battle_result']['status'] == '战败':
                seconds = current_config_storage['battle_result']['time_sleep']
                sc_cron_add_jobs(task_next_fn.pop(0), [task_id], task_id, seconds)
            elif current_config_storage['battle_result']['status'] == '平局':
                # 判断平局要求，是否等待，然后触发撤回的函数
                person = current_config_storage['battle_result']['person']
                enemy = current_config_storage['battle_result']['enemy']
                # 默认平局就撤退
                current_date = get_current_date(1)
                sc_cron_add_jobs(handle_battle_draw_result, [task_id], task_id, 1)
                # 添加等待任务
        # 平局 撤退步骤
        elif current_config_storage['type'] == 4:
            if current_config_storage['status'] == 0:
                seconds = current_config_storage['times']
                sc_cron_add_jobs(task_next_fn.pop(0), [task_id], task_id, seconds)
        #  队伍征兵
        elif current_config_storage['type'] == 1:
            next_time = current_config_storage['times'] + 1
            delay_time = current_config_storage['delay_time']
            if delay_time > next_time:
                next_time = delay_time
            sc_cron_add_jobs(task_next_fn.pop(0), [task_id], task_id, next_time)
        #  点击标记选择土地出征
        elif current_config_storage['type'] == 5:
            if current_config_storage['offset'] == 0:
                return
            sc_cron_add_jobs(task_next_fn.pop(0), [task_id], task_id, 1)
        # 取消标记
        elif current_config_storage['type'] == 6:
            offset = current_config_storage['offset']
            if offset == 0:
                return None
            else:
                set_task_all(task_id, copy.deepcopy(task_next_fn) * 2)
            task_next_fn = get_task_all(task_id)
            sc_cron_add_jobs(task_next_fn.pop(0), [task_id], task_id, 1)
    result_queue.put(event)


def sc_cron_add_jobs(fn, li, task_name, seconds):
    current_data = get_current_date(seconds)
    scheduler.add_job(fn,
                      'cron',
                      id=task_name,
                      year=current_data['year'], month=current_data['month'], day=current_data['day'],
                      hour=current_data['hour'], minute=current_data['minute'], second=current_data['second'],
                      args=li,
                      misfire_grace_time=60 * 60
                      )

# if __name__ == '__main__':
#     scheduler.start()
#     sc_cron_add_jobs(demo, 2023, 10, 20, 15, 2, 0)
#     sc_cron_add_jobs(demo2, 2023, 10, 20, 15, 2, 0)
#     while True:
#         pass

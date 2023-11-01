from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

from dispatcher.status import result_queue
from dispatcher.task_group import get_task_all
from modules.pageSwitch.page_switch import handle_in_lists_action, handle_battel_draw_result
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
    print(object_dict)
    task_id = object_dict['job_id']
    result = object_dict['retval']
    task_next_fn = get_task_all(task_id)
    if len(task_next_fn) > 0:
        # 1.扫荡 -> 2.查看战报 -> 3.胜利-失败/平局

        # 出发/扫荡
        if result['type'] == 2:
            l = result['lists']
            seconds = result['times']
            current_date = get_current_date(seconds)
            # 如果没有体力 进行等待 再进行出发
            next_fn = task_next_fn.pop(0) if result['result'] is not None else handle_in_lists_action
            # 等待执行下一步任务
            sc_cron_add_jobs(next_fn, [l, seconds],
                             current_date['year'], current_date['month'], current_date['day'],
                             current_date['hour'], current_date['minute'], current_date['second'],
                             task_id)
        # 战报结果
        elif result['type'] == 3:
            l = result['lists']
            seconds = result['times']
            if result['result']['status'] == '胜利' or result['result']['status'] == '失败':
                current_date = get_current_date(seconds)
                sc_cron_add_jobs(task_next_fn.pop(0), [l],
                                 current_date['year'], current_date['month'], current_date['day'],
                                 current_date['hour'], current_date['minute'], current_date['second'],
                                 task_id)
            elif result['result']['status'] == '平局':
                # 判断平局要求，是否等待，然后触发撤回的函数
                person = result['result']['person']
                enemy = result['result']['enemy']
                # 默认平局就撤退
                current_date = get_current_date(1)
                sc_cron_add_jobs(handle_battel_draw_result, [l, seconds],
                                 current_date['year'], current_date['month'], current_date['day'],
                                 current_date['hour'], current_date['minute'], current_date['second'],
                                 task_id)
                # 添加等待任务

        elif result['type'] == 4:
            if result['status'] == 0:
                l = result['lists']
                seconds = result['times']
                current_date = get_current_date(seconds)
                sc_cron_add_jobs(task_next_fn.pop(0), [l],
                                 current_date['year'], current_date['month'], current_date['day'],
                                 current_date['hour'], current_date['minute'], current_date['second'],
                                 task_id
                                 )

        elif result['type'] == 1:
            current_lists = result['lists']
            next_time = result['times']
            current_date = get_current_date(next_time)
            sc_cron_add_jobs(task_next_fn.pop(0), [current_lists],
                             current_date['year'], current_date['month'], current_date['day'],
                             current_date['hour'], current_date['minute'], current_date['second'],
                             task_id)
    result_queue.put(event)


def sc_cron_add_jobs(fn, li, year, month, day, hour, minute, second, info_id):
    scheduler.add_job(fn,
                      'cron',
                      id=info_id,
                      year=year, month=month, day=day,
                      hour=hour, minute=minute, second=second,
                      args=li,
                      misfire_grace_time=60 * 60
                      )

# if __name__ == '__main__':
#     scheduler.start()
#     sc_cron_add_jobs(demo, 2023, 10, 20, 15, 2, 0)
#     sc_cron_add_jobs(demo2, 2023, 10, 20, 15, 2, 0)
#     while True:
#         pass

import datetime

from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

from dispatcher.status import result_queue
from modules.tasks.battle import battle
from modules.tasks.zhengbing import zhengbing
from modules.utils.main import get_current_date

# 创建调度器
scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)},
                                job_defaults={'misfire_grace_time': 10})


def start_scheduler():
    scheduler.start()
    scheduler.add_listener(job_executed, EVENT_JOB_EXECUTED)


# 在此处任务进行校验跟添加任务
def job_executed(event):
    task_result = {}
    object_dict = vars(event)
    result = object_dict['retval']
    # 1.扫荡 -> 2.查看战报 -> 3.胜利-失败/平局
    if result['type'] == 2:
        # 此处添加战报查看函数
        l = result['lists']
        seconds = result['times']
        current_date = get_current_date(seconds)
        sc_cron_add_jobs(battle, [l, seconds],
                         current_date['year'], current_date['month'], current_date['day'],
                         current_date['hour'], current_date['minute'], current_date['second'],
                         '')

    elif result['type'] == 3:
        if result['result']['status'] == '胜利' or result['result']['status'] == '失败':
            # 判断胜利要求 # 设置等待征兵延时 并返回结果，如果扫荡次数大于1，需要减少，并添加到队列中
            l = result['lists']
            seconds = result['times']
            current_date = get_current_date(seconds)
            sc_cron_add_jobs(zhengbing,[l],
                             current_date['year'], current_date['month'],current_date['day'],
                             current_date['hour'], current_date['minute'], current_date['second'],
                             '')
        elif result['result']['status'] == '平局':

            # 判断平局要求，是否等待，然后触发撤回的函数，设置征兵任务，扫荡次数大于一，减少并添加到新的队列中
            pass
    elif result['type'] == 1:
        task_result['code'] = 0
        task_result['result'] = result['result']
    result_queue.put(task_result)


def sc_cron_add_jobs(fn, li, year, month, day, hour, minute, second, info):
    scheduler.add_job(fn,
                      'cron',
                      year=year, month=month, day=day,
                      hour=hour, minute=minute, second=second,
                      args=[li],
                      misfire_grace_time=60 * 60
                      )


# if __name__ == '__main__':
#     scheduler.start()
#     sc_cron_add_jobs(demo, 2023, 10, 20, 15, 2, 0)
#     sc_cron_add_jobs(demo2, 2023, 10, 20, 15, 2, 0)
#     while True:
#         pass

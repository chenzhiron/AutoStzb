import datetime
import logging
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_MISSED, EVENT_JOB_MODIFIED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler

from dispatcher.execute_type_1 import execute_type_1
from dispatcher.execute_type_2 import execute_type_2
from dispatcher.general_prop import tasks_result

# 创建调度器
scheduler = BlockingScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)})


def start_scheduler():
    for task in tasks_result:
        if tasks_result[task]['type'] == 1:
            execute_type_1(tasks_result[task])
        elif tasks_result[task]['type'] == 2:
            execute_type_2(tasks_result[task])
    # 启动调度器
    scheduler.start()
    return scheduler


def return_scheduler():
    return scheduler


def task_start(event):
    print(str(event))


def tasks_end(event):
    times = datetime.datetime.strptime("2099/09/09 15:18:00", "%Y/%m/%d %H:%M:%S")
    scheduler.modify_job(event.job_id, next_run_time=times)
    jobs = scheduler.get_jobs()
    for v in jobs:
        print(str(v))
    print(str(event))


def task_modified(event):
    # 在此处进行任务排序
    logging.error('任务在程序外部修改change::::'+'1111111111')
    logging.error(str(event))
    print(str(event))


def tasks_missed(event):
    print(str(event))


def scheduler_set_addlistener():
    scheduler.add_listener(task_modified, EVENT_JOB_MODIFIED)
    scheduler.add_listener(tasks_missed, EVENT_JOB_MISSED)
    scheduler.add_listener(tasks_end, EVENT_JOB_EXECUTED)


scheduler_set_addlistener()

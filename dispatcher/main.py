import datetime
import logging

from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler
# 创建调度器
scheduler = BlockingScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)},
                              job_defaults={'misfire_grace_time': 3600})


def start_scheduler():
    scheduler.add_listener(ended,EVENT_JOB_EXECUTED)
    scheduler.start()
    return scheduler


def ended(event):
    print(event)


def return_scheduler():
    return scheduler
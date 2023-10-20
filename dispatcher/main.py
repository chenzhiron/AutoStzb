import datetime
import logging
import time

from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

# 创建调度器
scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)},
                                )


def job_executed(event):
    object_dict = vars(event)
    # 遍历字典并打印属性和值
    for attribute, value in object_dict.items():
        print(f"{attribute}: {value}")

    print(scheduler.get_jobs())


scheduler.add_listener(job_executed, EVENT_JOB_EXECUTED)


def demo():
    time.sleep(20)
    print(datetime.datetime.now())


def demo2():
    print(datetime.datetime.now())


def sc_cron_add_jobs(fn, year, month, day, hour, minute, second):
    l = len(scheduler.get_jobs())
    scheduler.add_job(fn,
                      'cron',
                      year=year, month=month, day=day,
                      hour=hour, minute=minute, second=second,
                      id=fn.__name__ + str(l)
                      )


if __name__ == '__main__':
    scheduler.start()
    sc_cron_add_jobs(demo, 2023, 10, 20, 15, 2, 0)
    sc_cron_add_jobs(demo2, 2023, 10, 20, 15, 2, 0)
    while True:
        pass

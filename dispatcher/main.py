import datetime

from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

# 创建调度器
scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)},
                                job_defaults={'misfire_grace_time': 10})


def start_scheduler():
    scheduler.start()


# 在此处任务进行校验跟添加任务， 征兵 看返回结果是啥，扫荡的话，需要计算时间误差，然后插入战报校验，/平局处理
def job_executed(event):
    object_dict = vars(event)
    # 遍历字典并打印属性和值
    for attribute, value in object_dict.items():
        print(f"{attribute}: {value}")

    print(scheduler.get_jobs())


scheduler.add_listener(job_executed, EVENT_JOB_EXECUTED)


def sc_cron_add_jobs(fn, li, year, month, day, hour, minute, second):
    l = len(scheduler.get_jobs())
    scheduler.add_job(fn,
                      'cron',
                      year=year, month=month, day=day,
                      hour=hour, minute=minute, second=second,
                      id=fn.__name__ + str(l),
                      args=[li],
                      misfire_grace_time=1
                      )
    print(len(scheduler.get_jobs()))
# if __name__ == '__main__':
#     scheduler.start()
#     sc_cron_add_jobs(demo, 2023, 10, 20, 15, 2, 0)
#     sc_cron_add_jobs(demo2, 2023, 10, 20, 15, 2, 0)
#     while True:
#         pass

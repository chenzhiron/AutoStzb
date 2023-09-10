import datetime
import logging
from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler
from communication.execute_task_config import return_task_config_obj,insertion_task_config

# 创建调度器
scheduler = BlockingScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)})


def start_scheduler():
    scheduler_set_addlistener()
    scheduler.start()
    return scheduler


def return_scheduler():
    return scheduler


def tasks_end(event):
    job_id = event.job_id
    result = event.retval
    tasks_config_obj = return_task_config_obj()
    if len(tasks_config_obj[job_id]) == 0:
        return
    if 'sd' in job_id:
        sd_task_event(job_id, result)


def sd_task_event(job_id, result):
    tasks_config_obj = return_task_config_obj()
    fn = tasks_config_obj[job_id].pop(0)
    times = result['times']
    lists = result['lists']
    if fn['handle'].__name__ == 'battle':
        if 'result' in result:
            if result['result'] == 'deuce':
                # 需要返回平局计算的耗时，先默认平局 300
                times = 300 - result['timed']
                insertion_task_config(job_id, fn)
            else:
                fn = tasks_config_obj[job_id].pop(0)
        # 当调用平局多次的时候， 队伍的出发时间跟回来时间就会出现问题
        scheduler.add_job(fn['handle'],
                          id=fn['id'],
                          trigger='date',
                          next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times),
                          args=[lists, times])

    elif fn['handle'].__name__ == 'zhengbing':
        times = result['times']
        going_list = result['lists']
        scheduler.add_job(fn['handle'],
                          id=fn['id'],
                          trigger='date',
                          next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times),
                          args=[going_list])



def scheduler_set_addlistener():
    scheduler.add_listener(tasks_end, EVENT_JOB_EXECUTED)

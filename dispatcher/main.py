import datetime
import logging
from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler
from communication.execute_task_config import return_task_config_obj, insertion_task_config

# 创建调度器
scheduler = BlockingScheduler(executors={'default': ThreadPoolExecutor(max_workers=1)},
                              job_defaults={'misfire_grace_time': 3600})


def start_scheduler():
    scheduler_set_addlistener()
    scheduler.start()
    return scheduler


def return_scheduler():
    return scheduler


def tasks_end(event):
    job_id = event.job_id
    result = event.retval
    logging.error(str(job_id))
    logging.error(str(result))
    tasks_config_obj = return_task_config_obj()
    if len(tasks_config_obj[job_id]) == 0:
        return
    if 'sd' in job_id:
        sd_task_event(job_id, result)
    if 'list' in job_id:
        list_task_event(job_id, result)


def list_task_event(job_id, result):
    tasks_config_obj = return_task_config_obj()
    fn = tasks_config_obj[job_id].pop(0)
    # 该位置涉及多轮征兵问题
    # lists = result['lists']
    # times = result['times']
    # scheduler.add_job(fn['handle'], 'date',
    #                   next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times),
    #                   args=[lists])


def sd_task_event(job_id, result):
    tasks_config_obj = return_task_config_obj()
    fn = tasks_config_obj[job_id].pop(0)
    times = result['times']
    lists = result['lists']
    if fn['handle'].__name__ == 'battle':
        if 'result' in result:
            if result['result'] == 'deuce':
                times = 300 - times
            else:
                while fn['handle'].__name__ != 'battle':
                    fn = tasks_config_obj[job_id].pop(0)

    argss = [lists, times] if fn['handle'].__name__ == 'battle' else [lists]
    scheduler.add_job(fn['handle'],
                      id=fn['id'],
                      trigger='date',
                      next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times),
                      args=argss)


def scheduler_set_addlistener():
    scheduler.add_listener(tasks_end, EVENT_JOB_EXECUTED)

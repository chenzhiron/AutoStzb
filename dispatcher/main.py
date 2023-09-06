import logging

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_SCHEDULER_STARTED
from apscheduler.schedulers.background import BlockingScheduler

# 创建调度器
scheduler = BlockingScheduler()
scheduler.configure(misfire_grace_time=60*60, max_instances=1)
job_state_obj = {
    'state': False
}


def set_scheduler_state(event):
    logging.info('event:::::::::' + str(event)+'\n\r')
    job_state_obj['state'] = not job_state_obj['state']


def get_scheduler_state():
    return job_state_obj['state']


def start_scheduler():
    # 启动调度器
    scheduler.start()
    return scheduler


def return_scheduler():
    return scheduler


scheduler.add_listener(set_scheduler_state, EVENT_SCHEDULER_STARTED)
scheduler.add_listener(set_scheduler_state, EVENT_JOB_EXECUTED)

from tasks.saodang import saodang
from tasks.zhengbing import zhengbing
from datetime import datetime
import logging

name_saodang = 'saodang'
name_zhengbing = 'zhengbing'

from dispatcher.main import return_scheduler


def execute_tasks(task_list):
    scheduler = return_scheduler()
    logging.info('task module start')
    if name_zhengbing in task_list.keys():
        i = task_list[name_zhengbing]['team']
        scheduler.add_job(zhengbing, 'date', args=[i], next_run_time=datetime.now(), max_instances=1)

    if name_saodang in task_list.keys():
        i = task_list[name_saodang]['team']
        num = task_list[name_saodang]['number']
        scheduler.add_job(saodang, 'date', args=[i, num], next_run_time=datetime.now(), max_instances=1)

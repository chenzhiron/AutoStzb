from tasks.saodang import saodang
from tasks.zhengbing import zhengbing
from datetime import datetime
import logging
name_saodang = 'saodang'
name_zhengbing = 'zhengbing'

from dispatcher.main import start_scheduler


def execute_tasks(task_list):
    scheduler = start_scheduler()
    if name_zhengbing in task_list.keys():
        i = task_list[name_zhengbing]['team']
        scheduler.add_job(zhengbing, 'date', args=[i], next_run_time=datetime.now(), max_instances=1,
                          id=zhengbing.__name__)
        logging.info('end')
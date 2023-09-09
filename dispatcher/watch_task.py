import logging

import datetime


def execute_task_list(task_config):
    logging.error('99999999999999999999999999')
    from dispatcher.init_task_store import clear_task_store
    from dispatcher.main import return_scheduler
    scheduler = return_scheduler()
    for v in task_config:
        scheduler.modify_job(v['id'], next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=1))
    clear_task_store()

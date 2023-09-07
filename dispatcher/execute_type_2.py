import datetime

from tasks.saodang import saodang
from communication.task_store import change_store_data_value


def execute_type_2(task_config):
    from dispatcher.main import return_scheduler
    scheduler = return_scheduler()
    i = task_config['list']
    max_num = task_config['number']
    task_id = task_config['id']
    scheduler.add_job(
        saodang, 'date', args=[i, task_id], next_run_time=datetime.datetime.now()
    )
    if not scheduler.running:
        scheduler.start()
    change_store_data_value(task_id, 'number', max_num - 1)

import datetime

from dispatcher.main import return_scheduler
from tasks.zhengbing import zhengbing
scheduler = return_scheduler()


def execute_type_1(task_config):
    i = task_config['list']
    result = scheduler.add_job(
        zhengbing, 'date', args=[i], next_run_time=datetime.datetime.now()
    )
    if not scheduler.running:
        scheduler.start()
    else:
        pass
    # logging.info(result)
    return True


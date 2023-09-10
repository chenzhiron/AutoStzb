import datetime
from communication.execute_task_config import return_task_config_obj


def execute_task_list(task_config):
    from dispatcher.init_task_store import clear_task_store
    from dispatcher.main import return_scheduler
    scheduler = return_scheduler()
    task_config_obj = return_task_config_obj()
    for v in task_config:
        fn = task_config_obj[v['id']].pop(0)
        go_list = v['list']
        scheduler.add_job(
            fn['handle'],
            id=fn['id'],
            trigger='date',
            next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=1),
            args=[go_list]
        )
    clear_task_store()

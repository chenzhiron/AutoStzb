import datetime
from dispatcher.general_prop import trigger
from tasks.saodang import saodang


def execute_type_2(task_config):
    from dispatcher.main import return_scheduler
    scheduler = return_scheduler()
    i = task_config['list']
    id = task_config['id']
    times = datetime.datetime.strptime(task_config['next_execute'],"%Y/%m/%d %H:%M:%S")
    scheduler.add_job(saodang, trigger=trigger, args=[i, id], id=id, next_run_time=times,misfire_grace_time=1)
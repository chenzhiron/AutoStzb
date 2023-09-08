import datetime

from dispatcher.main import get_scheduler_status
from tasks.zhengbing import zhengbing

from communication.task_store import del_store_data


def execute_type_1(task_config):
    from dispatcher.main import return_scheduler
    scheduler = return_scheduler()
    current_time = datetime.datetime.now()
    if get_scheduler_status():
        current_time = current_time + datetime.timedelta(seconds=5)
    i = task_config['list']
    scheduler.add_job(
        zhengbing, 'date', args=[i], next_run_time=current_time
    )
    if not scheduler.running:
        scheduler.start()
    else:
        pass
    # 次数需要考虑到征兵队列为3，但征兵队伍有5个，先暂时默认征兵一定成功
    del_store_data(task_config['id'])

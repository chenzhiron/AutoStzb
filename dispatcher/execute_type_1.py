import datetime

from tasks.zhengbing import zhengbing

from communication.task_store import del_store_data


def execute_type_1(task_config):
    from dispatcher.main import return_scheduler
    scheduler = return_scheduler()
    i = task_config['list']
    scheduler.add_job(
        zhengbing, 'date', args=[i], next_run_time=datetime.datetime.now()
    )
    if not scheduler.running:
        scheduler.start()
    else:
        pass
    # 次数需要考虑到征兵队列为3，但征兵队伍有5个，先暂时默认征兵一定成功
    del_store_data(task_config['id'])

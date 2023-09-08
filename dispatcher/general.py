import datetime

from communication.task_store import get_store_data_value, get_store_data, del_store_data
from dispatcher.main import return_scheduler
from modules.module_battle.module_draw import module_computed_draw
from tasks.zhengbing import zhengbing


def battle_dispose_result(event):
    scheduler = return_scheduler()
    event_job_id = event.job_id
    if 'saodang' in event_job_id:
        battle_result = event.retval
        task_id = battle_result['task_id']
        time_seconds = get_store_data_value(task_id, 'next_execute')
        times = battle_result['times']
        # 胜利或者失败
        if battle_result['result'] == 'success' or battle_result['result'] == 'lose':
            result_list = get_store_data_value(task_id, 'list')

            scheduler.add_job(zhengbing, 'date',
                              args=[result_list, task_id],
                              next_run_time=datetime.datetime.now() + datetime.timedelta(
                                  seconds=time_seconds - times if time_seconds - times >= 0 else 0
                                ),
                              id=str(task_id) + zhengbing.__name__ + str(result_list)
                              )
        else:
            # 平局处理
            scheduler.add_job(module_computed_draw, 'date', args=[datetime.datetime.now().timestamp(), task_id],
                              next_run_time=datetime.datetime.now() + datetime.timedelta(
                                  seconds=(10 * 6 * 5) - times if (10 * 6 * 5) - times >= 0 else 0
                              ),
                              id=str(task_id) + 'saodang')
            pass


def zhengbing_dispose_result(event):
    scheduler = return_scheduler()
    event_job_id = event.job_id
    if 'zhengbing' in event_job_id:
        zhengbing_result = event.retval
        times = zhengbing_result['maxtime']
        task_id = zhengbing_result['task_id']
        task_config = get_store_data(task_id)
        if task_config['number'] == 0:
            del_store_data(task_id)
        else:
            from tasks.saodang import saodang
            scheduler.add_job(saodang,
                              'date',
                              args=[task_config['list'],
                                    task_config['id']],
                              next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times))

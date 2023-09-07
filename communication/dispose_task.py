from communication.task_store import add_store_data
from dispatcher.execute_type_1 import execute_type_1
from dispatcher.execute_type_2 import execute_type_2
from dispatcher.main import get_scheduler_status


async def dispose_task(websocket, task_config):
    from communication.comsumer import get_task
    if type(task_config) == int or type(task_config) == str and get_scheduler_status():
        await websocket.send(get_task)
        return
    add_store_data(task_config['id'], task_config)
    if task_config['type'] == 1:
        execute_type_1(task_config)
    if task_config['type'] == 2:
        execute_type_2(task_config)


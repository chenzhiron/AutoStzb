from dispatcher.init_task_store import append_task_store
from communication.execute_task_config import add_task_config_obj


async def dispose_task(websocket, task_config):
    from communication.comsumer import get_task
    if type(task_config) == int or type(task_config) == str:
        await websocket.send(get_task)
        return
    else:
        add_task_config_obj(task_config)
        append_task_store(task_config)
        await websocket.send(get_task)

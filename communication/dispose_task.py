from dispatcher.init_task_store import append_task_store


async def dispose_task(websocket, task_config):
    from communication.comsumer import get_task
    if type(task_config) == int or type(task_config) == str:
        await websocket.send(get_task)
        return
    append_task_store(task_config)

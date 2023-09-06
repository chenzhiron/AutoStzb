import time

import logging

from dispatcher.execute_type_1 import execute_type_1


async def dispose_task(websocket, task_config):
    from communication.comsumer import get_task
    if type(task_config) == int or type(task_config) == str:
        return
    logging.info(task_config)
    if task_config['type'] == 1:
        result = execute_type_1(task_config)
        if result:
            await websocket.send(get_task)
    if task_config['type'] == 2:
        time.sleep(5)
        await websocket.send(get_task)

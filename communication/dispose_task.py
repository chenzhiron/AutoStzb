import time

import logging


async def dispose_task(websocket, task_config):
    from communication.comsumer import get_task
    logging.info(task_config)
    await websocket.send(get_task)
    pass

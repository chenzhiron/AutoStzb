import queue
import logging

import threading
import time

from dispatcher.main import get_scheduler_state
from tasks.main import execute_tasks

task_queue = queue.Queue()


def return_task_queue():
    return task_queue


def start_queue():
    while True:
        job_state = get_scheduler_state()
        if not job_state:
            message = task_queue.get()
            if 'zhengbing' in message or 'saodang' in message:
                if message.get('zhengbing') is not None or message.get('saodang') is not None:
                    execute_tasks(message)
            else:
                logging.info(33333333333)
        time.sleep(1)


def start_queue_thread():
    queue_thread = threading.Thread(target=start_queue)
    queue_thread.start()

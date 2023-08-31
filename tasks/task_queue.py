import queue
import logging

from tasks.main import execute_tasks

task_queue = queue.Queue()


def return_task_queue():
    return task_queue


def start_queue():
    while True:
        message = task_queue.get()
        logging.info(message)
        if 'zhengbing' in message or 'saodang' in message:
            if message.get('zhengbing') is not None or message.get('saodang') is not None:
                execute_tasks(message)
        else:
            logging.info(33333333333)

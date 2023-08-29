from apscheduler.schedulers.blocking import BlockingScheduler

import json

scheduler = 0


def dispatcher_start():
    global scheduler
    scheduler = BlockingScheduler()
    return scheduler


def return_dispatcher():
    return scheduler


def my_task():
    print("Hello, world!")
    scheduler.remove_job('my_task')


def my_task2():
    print("222333")


if __name__ == '__main__':
    with open('../config/tasks.json') as file:
        tasks = json.load(file)
    print(tasks['zhengbing'])
    print(tasks)
    # dispatcher_start()
    # res = scheduler.add_job(my_task, 'interval', seconds=2, id=my_task.__name__)  # 每隔 5 秒执行一次任务
    # scheduler.start()

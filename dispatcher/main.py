from apscheduler.schedulers.blocking import BlockingScheduler


def my_task():
    print("Hello, world!")
    scheduler.remove_job('my_task')



def my_task2():
    print("222333")


scheduler = BlockingScheduler()
if __name__ == '__main__':
    res = scheduler.add_job(my_task, 'interval', seconds=2, id=my_task.__name__)  # 每隔 5 秒执行一次任务
    scheduler.start()

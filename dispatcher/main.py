from apscheduler.schedulers.blocking import BlockingScheduler


def my_task():
    print("Hello, world!")
    scheduler.add_job(my_task2, 'interval', seconds=2)
def my_task2():
    print("222333")


scheduler = BlockingScheduler()
if __name__ == '__main__':
    scheduler.add_job(my_task, 'interval', seconds=2)  # 每隔 5 秒执行一次任务
    scheduler.start()
    scheduler.remove_job('my_task')

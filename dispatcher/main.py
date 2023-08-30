from apscheduler.schedulers.background import BackgroundScheduler

# 创建调度器
scheduler = BackgroundScheduler()


# 定义要执行的任务
def job():
    print("Hello, World!")

def start_scheduler():
    # 启动调度器
    scheduler.start()
    return scheduler

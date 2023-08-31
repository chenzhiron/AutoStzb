from apscheduler.schedulers.background import BackgroundScheduler

# 创建调度器
scheduler = BackgroundScheduler()


def start_scheduler():
    # 启动调度器
    scheduler.start()
    return scheduler


def return_scheduler():
    return scheduler

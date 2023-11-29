from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from modules.utils import get_current_date


class Dispatcher:
    def __init__(self):
        self.status = False
        self.scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(1)})
        self.scheduler.add_listener(self.event_executed, EVENT_JOB_EXECUTED)

    # 任务执行完毕调用下一个任务
    def event_executed(self, event):
        from config.task_or_web_common import update_queue
        object_dict = vars(event)
        instance = object_dict['retval']
        instance.next_task()
        update_queue.put('update')

    def start(self):
        self.status = True
        self.scheduler.start()

    def stop(self):
        self.status = False
        self.scheduler.shutdown()

    def sc_cron_add_jobs(self, fn, arg, seconds):
        current_data = get_current_date(seconds)
        self.scheduler.add_job(fn,
                               'date',
                               args=arg,
                               next_run_time=current_data,
                               misfire_grace_time=60 * 60 * 24
                               )


task_dispatcher = Dispatcher()
# if task_dispatcher.scheduler.running:
#     pass
# else:
#     task_dispatcher.start()

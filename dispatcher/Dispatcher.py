from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_REMOVED
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from modules.utils.main import get_current_date


class Dispatcher:
    def __init__(self):
        self.current_instance_task = None
        self.scheduler = BackgroundScheduler(executors={'default': ThreadPoolExecutor(1)})
        self.scheduler.add_listener(self.event_executed, EVENT_JOB_EXECUTED)
        self.scheduler.add_listener(self.event_remove, EVENT_JOB_REMOVED)

    def event_remove(self, event):
        self.current_instance_task.next_task()

    def event_executed(self, event):
        object_dict = vars(event)
        instance = object_dict['retval']
        print(instance, 'result')
        self.current_instance_task = instance

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()

    def sc_cron_add_jobs(self, fn, arg, task_id, seconds):
        current_data = get_current_date(seconds)
        print(current_data)
        self.scheduler.add_job(fn,
                               'date',
                               id=task_id,
                               args=arg,
                               next_run_time=current_data,
                               misfire_grace_time=60 * 60
                               )


task_dispatcher = Dispatcher()
if task_dispatcher.scheduler.running:
    pass
else:
    task_dispatcher.start()

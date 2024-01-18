import time
from datetime import timedelta, datetime

from pywebio.output import use_scope, put_button, put_text

from config.config import globalConfig
from modules.task.tasks import taskManager


class Stzb:
    stop_event = False

    def __init__(self):
        self.device = None
        self.taskManagers = taskManager

    def change_config(self):
        self.stop_event = not self.stop_event
        try:
            if self.stop_event:
                self.devices()
                self.device.startDevices()
            else:
                self.device.closeDevice()
            self.render()
        except Exception as e:
            self.stop_event = False
            self.render()
            print(e)

    def render(self):
        with use_scope('scheduler', clear=True):
            put_text('调度器状态').style('display:inline-block;')
            put_button('运行中' if self.stop_event else '启动', onclick=self.change_config).style('display:inline-block;')

    def devices(self):
        from modules.devices.device import Devices
        self.device = Devices(globalConfig)
        return self.device

    def get_next_task(self):
        while 1:
            if self.stop_event:
                task = self.taskManagers.get_tasks()
                if task is None:
                    time.sleep(5)
                else:
                    return task
            time.sleep(5)

    def wait_until(self, future):
        future = future + timedelta(seconds=1)
        while 1:
            if datetime.now() > future:
                return True
            else:
                time.sleep(5)

    def run(self, task, command):
        return self.__getattribute__(command)(task)

    def loop(self):
        while 1:
            if self.stop_event:
                task = self.get_next_task()
                self.wait_until(task.next_run_times)
                try:
                    success = self.run(task, task.execute_tasks.pop(0))
                    print(task, success)
                except IndexError as e:
                    print('task null', e)
            time.sleep(5)

    def zhengbing(self, instance):
        for i in range(10):
            start = time.time()
            self.device.getScreenshots()
            print('zhengbing', time.time() - start)
        print('zhengbing', instance.next_run_times)
        return True

    def chuzheng(self, instance):
        print('chuzheng', instance.next_run_times)
        return True

    def saodang(self, instance):
        print('saodang', instance.next_run_times)
        return True


stzb = Stzb()
# if __name__ == '__main__':
#     stzb = Stzb()
#     stzb.loop()

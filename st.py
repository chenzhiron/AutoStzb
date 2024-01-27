import time
from datetime import timedelta, datetime

from pywebio.output import use_scope, put_button, put_text

from config.config import globalConfig
from modules.task.steps import ZhengBing


class Stzb:
    stop_event = False

    def __init__(self):
        self.device = None
        from modules.web.web import ui
        self.taskManagers = ui
        self.stData = None

    def change_config(self):
        self.stop_event = not self.stop_event
        # try:
        #     if self.stop_event:
        #         self.devices()
        #         self.device.startDevices()
        #     else:
        #         self.device.closeDevice()
        #         self.render()
        # except Exception as e:
        #     self.stop_event = False
        self.render()
        # print(e)

    def render(self):
        with use_scope('scheduler', clear=True):
            put_text('调度器状态').style('display:inline-block;')
            put_button('运行中' if self.stop_event else '启动', onclick=self.change_config).style(
                'display:inline-block;')

    def devices(self):
        from modules.devices.device import Devices
        self.device = Devices(globalConfig)
        return self.device

    def up_data(self):
        for v in self.stData['children']:
            if v['explain'] == 'next_run_time' and self.wait_until(v['value']):
                v['value'] = datetime.now()
        # change_data = self.taskManagers.get_main_data()
        self.taskManagers.update_main_refresh(self.stData)
        pass

    def wait_until(self, future):
        future = future + timedelta(seconds=1)
        if datetime.now() > future:
            return True
        else:
            return False

    def sort_tasks(self):
        while 1:
            self.stData = self.taskManagers.get_main_data()
            filtered_data = [
                unit for unit in self.stData['children']
                if any(child['explain'] == '状态' and child['value'] is True for child in unit['children']) and
                   any(child['explain'] == 'next_run_time' and child['value'] for child in unit['children'])
            ]
            sorted_data = sorted(
                filtered_data,
                key=lambda unit: datetime.strptime(
                    next(child['value'] for child in unit['children'] if child['explain'] == 'next_run_time'),
                    '%Y-%m-%d %H:%M:%S'
                )
            )
            if len(sorted_data) == 0:
                time.sleep(1)
                continue
            # 此处需要做额外的判断 包含 next_run_fn 为None情况
            next_run_time = 0
            for child in sorted_data[0]['children']:
                if child['explain'] == 'next_run_time':
                    next_run_time = child['value']
                    break
            if self.wait_until(datetime.strptime(next_run_time, '%Y-%m-%d %H:%M:%S')):
                return sorted_data[0]
            time.sleep(1)

    def get_next_task(self):
        while 1:
            if self.stop_event:
                task = self.sort_tasks()
                fn_name = None
                for v in task['children']:
                    if v['explain'] == 'next_run_fn':
                        fn_name = v['value']
                return task, fn_name

            time.sleep(5)

    def loop(self):
        while 1:
            if self.stop_event:
                task, fn = self.get_next_task()
                try:
                    print(task, fn)
                    self.run(task, fn)
                    self.up_data()
                except IndexError as e:
                    print('task null', e)
            time.sleep(5)

    def run(self, task, command):
        print('command', command)
        method = getattr(self, command, None)
        if method is not None:
            return method(task)
        else:
            raise AttributeError(f"Command '{command}' is not a valid method of {self.__class__.__name__}")

    def zhengbing(self, instance):
        ZhengBing(device=self.device, instance=instance).run()
        return True

    def chuzheng(self, instance):
        print('chuzheng', instance.next_run_times)
        return True

    def zhanbao(self, instance):
        print('zhanbao', instance.next_run_times)
        return True

    def saodang(self, instance):
        print('saodang', instance.next_run_times)
        return True


stzb = Stzb()
# if __name__ == '__main__':
#     stzb = Stzb()
#     stzb.loop()

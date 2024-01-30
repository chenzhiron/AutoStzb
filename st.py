import threading

import time
from datetime import timedelta, datetime

from pywebio.output import use_scope, put_button, put_text

from config.config import globalConfig
from modules.task.steps import ZhengBing
from modules.utils.utils import get_current_date


class Stzb:
    stop_event = False

    def __init__(self):
        self.device = None
        from modules.web.web import ui
        self.taskManagers = ui

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

    def up_data(self, task, execute_result):
        self.verify_next_tasks(task, execute_result)
        new_data = self.taskManagers.get_main_data()
        new_task = list(filter(lambda x: x['id'] == task['id'], new_data['children']))[0]
        new_task['children']['state']['value'] = task['children']['state']['value']
        new_task['children']['next_run_time']['value'] = task['children']['next_run_time']['value']
        new_task['children']['next_run_fn']['value'] = task['children']['next_run_fn']['value']
        new_task['children']['await_time']['value'] = task['children']['await_time']['value']
        print('task', task, 'execute_result', execute_result)
        self.taskManagers.update_main_refresh(new_data)

    def wait_until(self, future):
        future = future + timedelta(seconds=1)
        if datetime.now() > future:
            return True
        else:
            return False

    def sort_tasks(self):
        while 1:
            stData = self.taskManagers.get_main_data()
            filtered_data = []
            for v in stData['children']:
                for key, value in v['children'].items():
                    if key == 'state' and value['value']:
                        filtered_data.append(v)
            if len(filtered_data) == 0:
                time.sleep(1)
                continue
            filtered_data.sort(key=lambda x: x['children']['next_run_time']['value'])
            return filtered_data[0]

    # 对于任务函数，通过记录上一次执行的函数来计算下一次执行的函数任务
    def verify_next_tasks(self, config, result=None):
        if not isinstance(result, dict):
            return config
        current_task = config['children']
        # 校验征兵模块
        if result['type'] == 1:
            times = result['await_time']
            if times == 0:
                if current_task['mopping_up']['value'] != 0:
                    current_task['next_run_fn']['value'] = 'saodang'
                elif current_task['going']['value']:
                    current_task['next_run_fn']['value'] = 'chuzheng'
                else:
                    current_task['state']['value'] = False
            else:
                current_task['next_run_fn']['value'] = 'zhengbing'
            current_task['next_run_time']['value'] = get_current_date(times)
            current_task['await_time']['value'] = times
        del result['type']
        config.update(result)
        return config

    def get_next_task(self):
        while 1:
            if self.stop_event:
                task = self.sort_tasks()
                fn_name = None
                for key, v in task['children'].items():
                    if key == 'next_run_fn' and v['value'] is not None:
                        fn_name = v['value']
                return task, fn_name

            time.sleep(5)

    def loop(self):
        while 1:
            if self.stop_event:
                task, fn = self.get_next_task()
                print(task, fn)
                result = self.run(task, fn)
                print(result)
                self.up_data(task, result)
            time.sleep(5)

    def run(self, task, command):
        print('command', command)
        method = getattr(self, command, None)
        if method is not None:
            return method(task)
        else:
            raise AttributeError(f"Command '{command}' is not a valid method of {self.__class__.__name__}")

    def zhengbing(self, instance):
        # return ZhengBing(device=self.device, instance=instance).run()
        return {
            'type': 1,
            'await_time': 999
        }

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

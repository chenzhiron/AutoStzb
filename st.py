import time
from datetime import timedelta, datetime
from config.config import globalConfig
from modules.task.steps import ZhengBing
from modules.utils.utils import get_current_date
from modules.store.store import store


class Stzb:
    stop_event = False

    def __init__(self):
        self.device = None
        from modules.web.web import ui
        self.taskManagers = ui
        self.store = store

    def devices(self):
        from modules.devices.device import Devices
        self.device = Devices(globalConfig)
        return self.device

    def up_data(self, task, execute_result):
        task = self.verify_next_tasks(task, execute_result)
        new_data = self.taskManagers.get_main_data()
        new_task = list(filter(lambda x: x['id'] == task['id'], new_data['children']))[0]
        new_task['children']['state']['value'] = task['children']['state']['value']
        new_task['children']['next_run_time']['value'] = task['children']['next_run_time']['value']
        new_task['children']['next_run_fn']['value'] = task['children']['next_run_fn']['value']
        new_task['children']['await_time']['value'] = task['children']['await_time']['value']
        print('task', task, 'execute_result', execute_result)
        self.store.add_store(new_data)

    def wait_until(self, future):
        # 如果future是字符串类型，尝试将其解析为datetime对象
        if isinstance(future, str):
            try:
                future = datetime.fromisoformat(future)
            except ValueError:
                raise ValueError("future string is not in the correct format")

        # 如果future不是datetime类型，抛出错误
        elif not isinstance(future, datetime):
            raise TypeError("future must be a datetime object or a valid datetime string")

        # 在future上增加1秒
        future += timedelta(seconds=1)

        # 返回是否已经到达或超过future时间
        return datetime.now() >= future

    def sort_tasks(self):
        while 1:
            stData = self.taskManagers.get_main_data()
            filtered_data = []
            for v in stData['children']:
                for key, value in v['children'].items():
                    if key == 'state' and value['value']:
                        filtered_data.append(v)
            if len(filtered_data) == 0:
                time.sleep(2)
                continue
            filtered_data.sort(key=lambda x: x['children']['next_run_time']['value'])
            current_task_tims = filtered_data[0]['children']['next_run_time']['value']
            if self.wait_until(current_task_tims):
                return filtered_data[0]
            time.sleep(2)

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
        return config

    def get_next_task(self):
        while 1:
            if self.taskManagers.get_state():
                task = self.sort_tasks()
                fn_name = None
                for key, v in task['children'].items():
                    if key == 'next_run_fn' and v['value'] is not None:
                        fn_name = v['value']
                return task, fn_name
            time.sleep(5)

    def loop(self):
        while 1:
            if self.taskManagers.get_state():
                if self.device is None:
                    self.devices()
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
        return ZhengBing(device=self.device, instance=instance).run()
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

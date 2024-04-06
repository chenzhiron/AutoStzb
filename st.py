import time
from datetime import timedelta, datetime
from config.config import globalConfig
from modules.task.steps import *
from modules.utils.utils import get_current_date
from modules.web.web import ui

class Stzb:
    def __init__(self):
        self.device = None
        self.taskManagers = ui

    def devices(self, simulator=None):
        from modules.devices.device import Devices
        if simulator != None:
            globalConfig['Simulator']['url'] = simulator
        self.device = Devices(globalConfig)
        return self.device
    
    # 对于任务函数，通过记录上一次执行的函数来计算下一次执行的函数任务
    def task_updata(self, task, execute_result):
        # 未完成全部征兵,资源不够无法一次性拉完+5分钟等待
        if execute_result['type'] == 'ZhengBing' and execute_result['await_time'] != 0:
            task['next_run_time'] = datetime.now() + timedelta(seconds=execute_result['await_time'] + 300)
            self.taskManagers.set_data()
            return None
        # 已完成全部征兵
        if execute_result['type'] == 'ZhengBing' and execute_result['await_time'] == 0:
            task['next_run_time'] = datetime.now() + timedelta(seconds=1)
            task['recruit_person'] = False
            self.taskManagers.set_data()
            return None
        
        
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
            stData = self.taskManagers.get_data()
            print('stData', stData)
            filtered_data = []
            for v in stData['task']:
               if v['state']:
                    filtered_data.append(v)
            if len(filtered_data) == 0:
                time.sleep(2)
                continue
            filtered_data.sort(key=lambda x: x['next_run_time'])
            current_task_tims = filtered_data[0]['next_run_time']
            if self.wait_until(current_task_tims):
                return filtered_data[0]
            time.sleep(2)

    def get_next_task(self):
        while 1:
            if self.taskManagers.get_data('state'):
                task = self.sort_tasks()
                if task['recruit_person'] == True:
                    return task, 'zhengbing'
                if task['going'] == True:
                    if task['step'] == 0:
                        return task, 'chuzheng'
                    if task['step'] == 1:
                        return task, 'zhanbao'
                    if task['step'] == 2:
                        return task, 'chetui'
                    if task['step'] == 3:
                        return task, 'zhengbing'
                if task['mopping_up'] == True:
                    if task['step'] == 0:
                        return task, 'saodang'
                    if task['step'] == 1:
                        return task, 'zhanbao'
                    if task['step'] == 2:
                        return task, 'chetui'
                    if task['step'] == 3:
                        return task, 'zhengbing'
            time.sleep(5)

    def loop(self):
        self.devices()
        while 1:
            res = self.taskManagers.get_data()
            if res['state'] == 1:
                if res['simulator'] != globalConfig['Simulator']['url'] or self.device is None:
                    self.devices(res['simulator'])
                task, fn = self.get_next_task()
                print(task, fn)
                result = self.run(task, fn)
                print(result)
                self.task_updata(task, result)
            time.sleep(3)

    def run(self, task, command):
        print('command', command)
        method = getattr(self, command, None)
        if method is not None:
            return method(task)
        else:
            raise AttributeError(f"Command '{command}' is not a valid method of {self.__class__.__name__}")

    def zhengbing(self, instance):
        #  {"type": ZhengBing, "await_time": 0 | 1-Max}
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

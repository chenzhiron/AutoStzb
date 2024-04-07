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

        if execute_result['type'] == 'ChuZheng':
            if task['_step'] == 1:
                task['next_run_time'] = (datetime.now() + timedelta(seconds=execute_result['_speed_time'])).strftime("%Y-%m-%d %H:%M:%S")
                task['x'] = ','.join(task['x'])
                task['y'] = ','.join(task['y'])
            elif task['_step'] == 2:
                task['next_run_time'] = (datetime.now() + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
            elif task['_step'] == 3:
                task['next_run_time'] = (datetime.now() + timedelta(seconds=execute_result['_speed_time'])).strftime("%Y-%m-%d %H:%M:%S")
                task['x'].pop(0)
                task['y'].pop(0)
                if len(task['x']) == 0 or len(task['y']) == 0:
                    task['going'] = False
                task['x'] = ','.join(task['x'])
                task['y'] = ','.join(task['y'])
            self.taskManagers.set_data('task', task, task['id'])

        elif execute_result['type'] == 'SaoDang':
            if task['_step'] == 1 or task['_step'] == 3:
                task['next_run_time'] = (datetime.now() + timedelta(seconds=execute_result['_speed_time'])).strftime("%Y-%m-%d %H:%M:%S")
                task['x'] = ','.join(task['x'])
                task['y'] = ','.join(task['y'])
            elif task['_step'] == 2:
                task['next_run_time'] = (datetime.now() + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
            self.taskManagers.set_data('task', task, task['id'])

        elif execute_result['type'] == 'ZhengBing':
            if execute_result['await_time'] != 0 :
                if execute_result['await_time'] < 300:
                    execute_result['await_time'] += 300
                task['next_run_time'] = (datetime.now() + timedelta(seconds=execute_result['await_time'])).strftime("%Y-%m-%d %H:%M:%S")
                self.taskManagers.set_data('task', task, task['id'])
            else:
                task['next_run_time'] = (datetime.now() + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
                task['recruit_person'] = False
                self.taskManagers.set_data('task', task, task['id'])


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
               if v.get('_step') == None:
                    v['_step'] = 0
               if v['state']:
                    filtered_data.append(v)
                    if len(v['x']) > 0:
                        v['x'] = v['x'].split(',')
                    if len(v['y']) > 0:
                        v['y'] = v['y'].split(',')
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
                if task['going']:
                    if task['_step'] == 0:
                        return task, 'chuzheng'
                    if task['_step'] == 1:
                        return task, 'zhanbao'
                    if task['_step'] == 2:
                        return task, 'chetui'
                    if task['_step'] == 3 and task['recruit_person']:
                        return task, 'zhengbing'
                    else:
                        return task, 'chuzheng'
                if task['mopping_up']:
                    if task['_step'] == 0:
                        return task, 'saodang'
                    if task['_step'] == 1:
                        return task, 'zhanbao'
                    if task['_step'] == 2:
                        return task, 'chetui'
                    if task['_step'] == 3 and task['recruit_person']:
                        return task, 'zhengbing'
                    else:
                        return task, 'saodang'
                if task['recruit_person']:
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
        return ChuZheng(device=self.device, instance=instance).run()

    def zhanbao(self, instance):
        return ZhanBao(device=self.device, instance=instance).run()
    def chetui(self, instance):
        return PingJuChetui(device=self.device, instance=instance).run()
    def saodang(self, instance):
        return SaoDang(device=self.device, instance=instance).run()


stzb = Stzb()
# if __name__ == '__main__':
#     stzb = Stzb()
#     stzb.loop()

import time
from modules.task.steps import *
from modules.logs.logs import st_logger
from modules.manager.main import conf
from modules.devices.device import Devices
from modules.utils.utils import wait_until
class Stzb:
    def __init__(self):
        self.device = None
        self.simulator = None

    def initDevices(self):
        simulator_val = conf.get_key_data('simulator')['value']
        screen_await_val = conf.get_key_data('screen_await')['value']
        if self.device is None:
            self.device = Devices({
                "simulator": simulator_val,
                "screen_await": screen_await_val
            })
            self.simulator = simulator_val
            return self.device
        
        if self.simulator is not simulator_val:
            self.device = Devices({
                "simulator": simulator_val,
                "screen_await": screen_await_val
            })
            return self.device
    
 
    def get_next_run_time(self, item):
        nested_dict = item.get(list(item.keys())[0], {})
        return nested_dict.get('next_run_time', '')

    def sort_tasks(self):
        filtered_data = []
        execute_key = ['feat', 'troop1', 'troop2', 'troop3', 'troop4', 'troop5']
        task_data = conf.get_data()
        for key, value in task_data.items():
            if key not in execute_key:
                continue
            if value['state']:
                filtered_data.append({key:value})
        if len(filtered_data) == 0:
            return None
        filtered_data.sort(key=self.get_next_run_time)
        current_task_times = filtered_data[0][list(filtered_data[0].keys())[0]]['next_run_time']
        if wait_until(current_task_times):
            return filtered_data[0]
        return None
    
    def get_next_task(self):
        task = self.sort_tasks()
        if task is None:
            return (None, None)
        return next(iter(task.items()))
    
    def loop(self):
        while 1:
            res = conf.get_key_data('state')['value']
            if res:
                self.initDevices() 
                fnMane, fnObj = self.get_next_task()
                if fnMane is None or fnObj is None:
                    time.sleep(1)
                    continue
                st_logger.info('next task: %s %s', fnMane, fnObj)
                self.run(fnMane)
                print('任务结束', time.time())
            time.sleep(1)

    def run(self, fnMane):
        method = getattr(self, fnMane, None)
        if method is not None:
            return method()
        
    def feat(self):
        pass
        # return FeatStatis(self.device, 'feat').run()
    def troo1(self):
        pass
    def troop2(self):
        pass
    def troop3(self):
        pass
    def troop4(self):
        pass
    def troop5(self):
        pass
        
stzb = Stzb()
# if __name__ == '__main__':
#     stzb = Stzb()
#     stzb.loop()
  # def task_updata(self, task, execute_result):
    #     if execute_result['type'] == 'FeatOperatorSteps':
    #         task['state'] = False
    #         self.taskManagers.set_data('feat', task)
    #         return
    #     if execute_result['type'] == 'ChuZheng':
    #         task['next_run_time'] = (datetime.now() + timedelta(seconds=execute_result['_speed_time'])).strftime("%Y-%m-%d %H:%M:%S")
    #         task['x'] = ','.join(task['x'])
    #         task['y'] = ','.join(task['y'])
    #         task['_speed_time'] = execute_result['_speed_time']
    #         task['_step'] = execute_result['_step']
    #         self.taskManagers.set_data('task', task, task['id'])
    #         return
    #     elif execute_result['type'] == 'SaoDang':
    #         task['next_run_time'] = (datetime.now() + timedelta(seconds=execute_result['_speed_time'])).strftime("%Y-%m-%d %H:%M:%S")
    #         task['x'] = ','.join(task['x'])
    #         task['y'] = ','.join(task['y'])
    #         task['_speed_time'] = execute_result['_speed_time']
    #         task['_step'] = execute_result['_step']
    #         self.taskManagers.set_data('task', task, task['id'])
    #         return

    #     elif execute_result['type'] == 'ZhanBao':
    #         task['_step'] = execute_result['_step']
    #         task['battle_info'].append(execute_result['_battle_info'])
    #         # 出征
    #         if task['going'] and task['_step'] == 3:
    #             task['x'].pop(0)
    #             task['y'].pop(0)
    #             if len(task['x']) == 0 or len(task['y']) == 0:
    #                 task['going'] = False
            
    #         #     task['x'] = ','.join(task['x'])
    #         #     task['y'] = ','.join(task['y'])
    #         # elif task['mopping_up']:
    #         #     task['x'] = ','.join(task['x'])
    #         #     task['y'] = ','.join(task['y'])
    #         task['x'] = ','.join(task['x'])
    #         task['y'] = ','.join(task['y'])
    #         if task['_step'] == 1 and execute_result['_info_all']:
    #             task['next_run_time'] = (datetime.now() + timedelta(seconds=300)).strftime("%Y-%m-%d %H:%M:%S")
    #         elif task['_step'] == 2 and not execute_result['_info_all']:
    #             task['next_run_time'] = (datetime.now() + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
    #         else:
    #             task['next_run_time'] = (datetime.now() + timedelta(seconds=task['_speed_time'])).strftime("%Y-%m-%d %H:%M:%S")
    #         self.taskManagers.set_data('task', task, task['id'])
    #         return
    #     elif execute_result['type'] == 'ZhengBing':
    #         if execute_result['await_time'] != 0 :
    #             if execute_result['await_time'] < 300:
    #                 execute_result['await_time'] += 300
    #             task['next_run_time'] = (datetime.now() + timedelta(seconds=execute_result['await_time'])).strftime("%Y-%m-%d %H:%M:%S")
    #             self.taskManagers.set_data('task', task, task['id'])
    #         else:
    #             task['next_run_time'] = (datetime.now() + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
    #             task['_step'] = 0
    #             if not task['going'] and not task['mopping_up']:
    #                 task['recruit_person'] = False
    #             self.taskManagers.set_data('task', task, task['id'])
    #         return
    #     elif execute_result['type'] == 'PingJuChetui':
    #         task['_step'] = execute_result['_step']
    #         task['next_run_time'] = (datetime.now() + timedelta(seconds=task['_speed_time'])).strftime("%Y-%m-%d %H:%M:%S")
    #         self.taskManagers.set_data('task', task, task['id'])
    #         return

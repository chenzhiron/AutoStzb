import time

from modules.task.setups import *


class Origin:
    # 接收实例配置，但是不修改实例的任何属性，只读
    def __init__(self, device, instance):
        self.devices = device
        self.instance = instance
        self._step = 0
        self.tasks_result = {
            'type': None
        }

    def ret_main(self):
        return_main.run(self.devices)


class ZhengBing(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        self.exec_step = [verfiy_main, click_budui, click_zhengbing, swipe_zhengbing,
                          zhengbing_max_time, click_zhengbing_sure, click_zhengbing_require]
        

    def verifySteps(self):
        start_time = time.time()
        img = self.devices.getScreenshots()
        for index, fn in enumerate(self.exec_step):
            fn.verifyOcr(img)
            if fn.verifyTxt():
                self._step = index
        print('征兵一个判断图循环用时:', time.time() - start_time)

    def run(self):
        click_budui.x = self.instance['team'] * 200
        self.tasks_result['type'] = self.__class__.__name__
        # 先截一张图，看下当前的图出现元素有哪些，跳转到对应的位置，并继续下一步
        # 看下主页活动在不在，然后看下在不在势力，接着查看 征兵按钮，接着 查看 进度条页面，接着识别确认征兵
        # 添加实例的下一次运行时间校验
        self.verifySteps()
        start_time = time.time()
        print(self._step, '初始化 self._step')
        while self._step < len(self.exec_step):
            print(self._step, 'self._step')
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self._step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instance)
            print('函数运行结果', res, '当前运行的函数', task_instance)
            if res == False:
                continue
            self.tasks_result.update(res)
            if not res['next']:
                break
            self._step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('征兵超时')
        self.ret_main()
        return self.tasks_result


class ChuZheng(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        # 前置识图进入跳转页面
        self.exec_step = [click_big_land, click_land_x, click_land_y, click_land_require, click_land_center,
                          click_sign_land_chuzheng, click_going_lists, going_max_time, click_chuzheng]
        click_land_x.input_value = instance['x'][0]
        click_land_y.input_value = instance['y'][0]
        click_going_lists.x = instance['team'] * 220 - 60 + 220
    def run(self):
        self.tasks_result['_step'] = 1
        self.tasks_result['type'] = self.__class__.__name__
        start_time = time.time()
        while self._step < len(self.exec_step):
            print(self._step, 'self._step')
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self._step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instance)
            if res == False:
                continue
            self.tasks_result.update(res)
            if not res['next']:
                break
            self._step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('出征超时')
        self.ret_main()
        return self.tasks_result

class ZhanBao(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        self.exec_step = [verfiy_main_info, click_search_screen, click_search_x, click_search_y, click_search,
                          lists_status, search_persons, search_enemy]
        click_search_x.input_value = instance['x'][0]
        click_search_y.input_value = instance['y'][0]
        
    def run(self):
        self.tasks_result['type'] = self.__class__.__name__
        start_time = time.time()
        while self._step < len(self.exec_step):
            print(self._step, 'self._step')
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self._step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instance)
            if res == False:
                continue
            self.tasks_result.update(res)
            if not res['next']:
                break
            self._step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('战报超时')
        if self.tasks_result['_list_status'] == '胜' or self.tasks_result['_list_status'] == '败':
            self.tasks_result['_step'] = 3
            self.ret_main()
        else:
            person_status = float(self.tasks_result['person'][0]) > float(self.tasks_result['person'][1]) * float(self.instance['residue_troops_person'] )
            enemy_statue = float(self.tasks_result['enemy'][0]) < float(self.tasks_result['enemy'][1]) * float(self.instance['residue_troops_enemy'])
            if person_status and enemy_statue:
                self.tasks_result['_info_all'] = True
                self.tasks_result['_step'] = 1
                self.ret_main()
            else:
                self.tasks_result['_info_all'] = False
                self.tasks_result['_step'] = 2
            print('person_status', person_status, 'enemy_statue', enemy_statue)
        return self.tasks_result

class SaoDang(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        # 前置识图进入跳转页面
        self.exec_step = [click_big_land, click_land_x, click_land_y, click_land_require, click_land_center,
                        click_sign_land_saodang, click_going_lists, going_max_time, click_saodang]
        click_land_x.input_value = instance['x'][0]
        click_land_y.input_value = instance['y'][0]
        click_going_lists.x = instance['team'] * 220 - 60 + 220

    def run(self):
        self.tasks_result['_step'] = 1
        self.tasks_result['type'] = self.__class__.__name__
        start_time = time.time()
        while self._step < len(self.exec_step):
            print(self._step, 'self._step')
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self._step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instance)
            if res == False:
                continue
            self.tasks_result.update(res)
            if not res['next']:
                break
            self._step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('扫荡超时')
        self.ret_main()
        return self.tasks_result

class PingJuChetui(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        self.exec_step = [click_info_require, click_go_require, click_state_info,click_chetui,click_chetui_require]

    def run(self):
        self.tasks_result['_step'] = 3
        self.tasks_result['type'] = self.__class__.__name__
        start_time = time.time()
        while self._step < len(self.exec_step):
            print(self._step, 'self._step')
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self._step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instance)
            if res == False:
                continue
            self.tasks_result.update(res)
            if not res['next']:
                break
            self._step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('平局撤退超时')
        self.ret_main()
        return self.tasks_result

import time

from modules.task.setups import *


class Origin:
    # 接收实例配置，但是不修改实例的任何属性，只读
    def __init__(self, device, instance):
        self.devices = device
        self.instances = instance
        self.step = 0
        self.tasks_result = {
            'type': 1
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
                self.step = index
        print('征兵一个判断图循环用时:', time.time() - start_time)

    def run(self):
        # 先截一张图，看下当前的图出现元素有哪些，跳转到对应的位置，并继续下一步
        # 看下主页活动在不在，然后看下在不在势力，接着查看 征兵按钮，接着 查看 进度条页面，接着识别确认征兵
        # 添加实例的下一次运行时间校验
        self.verifySteps()
        start_time = time.time()
        print(self.step, '初始化 self.step')
        self.step -= 1
        while self.step < len(self.exec_step):
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self.step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instances)
            print('函数运行结果', res, '当前运行的函数', task_instance)
            if isinstance(res, dict):
                self.tasks_result.update(res)
                if not res['next']:
                        # 调取返回主页函数
                    return self.tasks_result
                self.step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('征兵超时')
        self.ret_main()
        return self.tasks_result


class ChuZheng(Origin):
    def __init__(self, devices, instance):
        super().__init__(devices, instance)
        # 前置识图进入跳转页面
        self.exec_step = [click_big_land, click_land_x, click_land_y, click_land_require, click_land_center,
                          click_sign_land_chuzheng, click_going_lists, going_max_time, click_chuzheng]
        click_land_x.input_value = instance['x']
        click_land_y.input_value = instance['y']

    def run(self):
        start_time = time.time()
        while self.step < len(self.exec_step):
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self.step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instances)
            if isinstance(res, dict):
                self.tasks_result.update(res)
                if not res['next']:
                    # 调取返回主页函数
                    return self.tasks_result
                self.step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('征兵超时')
        self.ret_main()
        return self.tasks_result

class Zhanbao(Origin):
    def __init__(self, devices, instance):
        super().__init__(devices, instance)
        self.exec_step = [verfiy_main_info, click_search_screen, click_search_x, click_search_y, click_search,
                          lists_status, search_persons, search_enemy]
        click_search_x.input_value = instance['x']
        click_search_y.input_value = instance['y']

    def run(self):
        start_time = time.time()
        while self.step < len(self.exec_step):
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self.step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instances)
            if isinstance(res, dict):
                self.tasks_result.update(res)
                if not res['next']:
                    # 调取返回主页函数
                    return self.tasks_result
                self.step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('战报超时')
        self.ret_main()
        return self.tasks_result

class Saodang(Origin):
    def __init__(self, devices, instance):
            super().__init__(devices, instance)
            # 前置识图进入跳转页面
            self.exec_step = [click_big_land, click_land_x, click_land_y, click_land_require, click_land_center,
                            click_sign_land_chuzheng, click_going_lists, going_max_time, click_saodang]
            click_land_x.input_value = instance['x']
            click_land_y.input_value = instance['y']

    def run(self):
        start_time = time.time()
        while self.step < len(self.exec_step):
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self.step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instances)
            if isinstance(res, dict):
                self.tasks_result.update(res)
                if not res['next']:
                    # 调取返回主页函数
                    return self.tasks_result
                self.step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('征兵超时')
        self.ret_main()
        return self.tasks_result

class PingJuChetui(Origin):
    def __init__(self, devices, instance):
            super().__init__(devices, instance)
            self.exec_step = [click_info_require, click_go_require,click_state_info,click_chetui,click_chetui_require]
    def run(self):
        start_time = time.time()
        while self.step < len(self.exec_step):
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self.step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instances)
            if isinstance(res, dict):
                self.tasks_result.update(res)
                if not res['next']:
                    # 调取返回主页函数
                    return self.tasks_result
                self.step += 1
            if time.time() - start_time > 60:
                raise TimeoutError('战报超时')
        self.ret_main()
        return self.tasks_result

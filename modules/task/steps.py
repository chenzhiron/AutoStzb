import time

from modules.task.setups import *


class Origin:
    # 接收实例配置，但是不修改实例的任何属性，只读
    def __init__(self, device, instance):
        self.devices = device
        self.instances = instance
        self.step = 0
        self.tasks_result = {
            type: 1
        }


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
        while self.step < len(self.exec_step):
            for i in range(10):
                img = self.devices.getScreenshots()
                task_instance = self.exec_step[self.step]
                task_instance.verifyOcr(img)
                res = task_instance.run(self.devices, self.instances)
                if isinstance(res, dict):
                    self.tasks_result.update(res)
                    self.step += 1
                    break
        return self.tasks_result


class Chuzheng(Origin):
    def __init__(self, devices, instance):
        super().__init__(devices, instance)

    def run(self):
        pass


class Zhanbao(Origin):
    def __init__(self, devices, instance):
        super().__init__(devices, instance)

    def run(self):
        pass


class Saodang(Origin):
    def __init__(self, devices, instance):
        super().__init__(devices, instance)

    def run(self):
        pass

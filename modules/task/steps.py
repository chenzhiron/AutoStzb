import time

from modules.task.setups import *


class Origin:
    def __init__(self, device, instance):
        self.devices = device
        self.instances = instance
        self.step = 0


class ZhengBing(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        self.exec_step = [verfiy_main, click_budui, click_zhengbing, swipe_zhengbing,
                          zhengbing_max_time, click_zhengbing_sure, click_zhengbing_require]

    def run(self):
        # 先截一张图，看下当前的图出现元素有哪些，跳转到对应的位置，并继续下一步
        # 看下主页活动在不在，然后看下在不在势力，接着查看 征兵按钮，接着 查看 进度条页面，接着识别确认征兵
        img = self.devices.getScreenshots()
        for index, fn in enumerate(self.exec_step):
            fn.verifyOcr(img)
            if fn.verifyTxt():
                self.step = index

        # 添加实例的下一次运行时间校验
        while self.step < len(self.exec_step):
            for i in range(30):
                img = self.devices.getScreenshots()
                task_instance = self.exec_step[self.step]
                task_instance.verifyOcr(img)
                if task_instance.run(self.devices, self.instances):
                    self.step += 1
                    break
                time.sleep(0.5)
        self.step = 0
        return True

        # # logger.info('开始征兵模块')
        # times = 0
        # # 需要捕获征兵队伍
        # while 1:
        #     if click_satify.applyClick():
        #         # logger.info('征兵已满')
        #         instance.change_config_storage_by_key('next_times', times)
        #         # if instance.type == zhengbingType:
        #         #     instance.change_config_storage_by_key('status', False)
        #         handle_out_home(instance)
        #         return instance
        #     if click_zhengbing_require.applyClick():
        #         # logger.info('确认确认征兵')
        #         instance.change_config_storage_by_key('next_times', times)
        #         # if instance.type == zhengbingType:
        #         #     instance.change_config_storage_by_key('setup', instance.setup - 1)
        #         handle_out_home(instance)
        #         return instance
        #     if swipe_zhengbing.applySwipe():
        #         # logger.info('滑动征兵进度条')
        #         times = zhengbing_max_time()
        #         # if instance.type == zhengbingType:
        #         #     times = times + 300
        #     if click_zhengbing.applyClick():
        #         # logger.info('点击征兵按钮')
        #         continue
        #     if click_budui.applyClick(instance.lists):
        #         # logger.info('选择主城部队')
        #         continue
        #     if click_shili.applyClick():
        #         # logger.info('选择势力')
        #         continue
        #     if click_zhengbing_sure.applyClick():
        #         # logger.info('确认征兵')
        #         continue


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

class zhengbing:
    exec_step = []

    def __init__(self, device, instance):
        self.device = device
        self.instance = instance
        self.step = 0

    def run(self):
        while self.step > len(self.exec_step):
            img = self.device.getScreenshots()
            if img is None:
                # 抛出异常
                return None
            task_instance = self.exec_step[self.step]
            task_instance.verifyOcr(img)
            res = self.exec_step[self.step].run(self.device, self.instance)
            if res:
                self.step += 1
            else:
                self.step -= 1
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

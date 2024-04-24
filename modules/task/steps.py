import time
from modules.task.setups import *
from modules.logs.logs import st_logger
from modules.utils.utils import img_bytes_like, export_xlsx
from modules.task.general.option_verify_area import address_execute_list
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
        click_budui.txt = instance['outset']

    def verifySteps(self):
        start_time = time.time()
        img = self.devices.getScreenshots()
        for index, fn in enumerate(self.exec_step):
            fn.verifyOcr(img)
            if fn.verifyTxt():
                self._step = index
        st_logger.info(self.__class__.__name__ + '  init_step:' + str(self._step))

    def run(self):
        self.tasks_result['type'] = self.__class__.__name__
        self.verifySteps()
        start_time = time.time()
        while self._step < len(self.exec_step):
            st_logger.info('execute step:' + str(self._step) + self.__class__.__name__)
            img = self.devices.getScreenshots()
            task_instance = self.exec_step[self._step]
            task_instance.verifyOcr(img)
            res = task_instance.run(self.devices, self.instance)
            if res == False:
                continue
            self.tasks_result.update(res)
            if not res['next']:
                start_time = time.time()
                break
            self._step += 1
            if time.time() - start_time > 20:
                raise TimeoutError('征兵超时')
        self.ret_main()
        return self.tasks_result


class ChuZheng(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        # 前置识图进入跳转页面
        self.exec_step = [click_big_land, click_land_x, click_land_y, click_land_require, click_land_center,
                          click_sign_land_chuzheng, search_going, click_going_lists, going_max_time, click_chuzheng]
        click_land_x.input_value = instance['x'][0]
        click_land_y.input_value = instance['y'][0]
        search_going.txt = instance['outset']
        sum = instance['standby_max']
        current_team = instance['team']
        click_going_lists.y = address_execute_list[sum-1][current_team-1][0]

    def run(self):
        self.tasks_result['_step'] = 1
        self.tasks_result['type'] = self.__class__.__name__
        start_time = time.time()
        while self._step < len(self.exec_step):
            st_logger.info('execute step:' + str(self._step) + self.__class__.__name__)
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
            st_logger.info('execute step:' + str(self._step) + self.__class__.__name__)
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
        self.tasks_result['_battle_info'] = img_bytes_like(self.devices.getScreenshots())
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
            st_logger.info('person_status:' + str(person_status) + '  enemy_statue:' + str(enemy_statue))
        return self.tasks_result

class SaoDang(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        # 前置识图进入跳转页面
        self.exec_step = [click_big_land, click_land_x, click_land_y, click_land_require, click_land_center,
                        click_sign_land_saodang, search_going, click_going_lists, going_max_time, click_saodang]
        click_land_x.input_value = instance['x'][0]
        click_land_y.input_value = instance['y'][0]
        search_going.txt = instance['outset']
        sum = instance['standby_max']
        current_team = instance['team']
        click_going_lists.y = address_execute_list[sum-1][current_team-1][0]

    def run(self):
        self.tasks_result['_step'] = 1
        self.tasks_result['type'] = self.__class__.__name__
        start_time = time.time()
        while self._step < len(self.exec_step):
            st_logger.info('execute step:' + str(self._step) + self.__class__.__name__)
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
            st_logger.info('execute step:' + str(self._step) + self.__class__.__name__)
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

class FeatStatis(Origin):
    def __init__(self, device, instance):
        super().__init__(device, instance)
        self.exec_step = [FeatOperatorSteps]

    def run(self, devices, instance):
        self.tasks_result['type'] = self.__class__.__name__
        while 1:
            res = self.run(self.exec_step[0], devices, instance)
            self.tasks_result.update(res)
            # 此处处理数据
            
            export_xlsx(export_xlsx, '武勋统计表')
            return self.tasks_result
            
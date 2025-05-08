import logging
import time

from modules.devices.main import DeviceOperator, DeviceManager
from modules.taskfn.basic import Basic
from modules.taskfn.steps_basic import StepsBasic
from modules.taskfn.tasks_utils import time_consuming, extract_numbers_from_brackets, time_str_to_seconds
from modules.utils import truncated_normal


class Capture(Basic):
    def __init__(self, operator, config):
        super().__init__(operator, config)
        self.steps_basic = StepsBasic(operator)
        self.map_x = 0
        self.map_y = 0
        self.time_sleep = 0

    def action_click(self):
        if self.steps_basic.verify_action_click():
            self.device.click(truncated_normal(375, 440), truncated_normal(735, 880))
            return True
        return None

    def action_list(self):
        if self.steps_basic.verify_action_list():
            if self.config['address'] == '':
                num = self.config['num']
                offset_x = 75 + ((170 + 40) * (num - 1))
                offset_x_end = 75 + (170 * num) + (40 * (num - 1))
                offset_y = 240 + 80
                offset_y_end = offset_y + 80
                print(offset_x, offset_x_end, offset_y, offset_y_end)
                self.device.click(truncated_normal(offset_x, offset_x_end), truncated_normal(offset_y, offset_y_end))
                return True
            return None
        return None

    def action_zhengbing(self):
        if self.steps_basic.verify_going_zhengbing():
            self.device.click(truncated_normal(735, 850), truncated_normal(665, 720))
            return True
        return None

    def action_zhengbing_max(self):
        if self.steps_basic.verify_zhengbing_page():
            self.device.click(truncated_normal(1135, 1280), truncated_normal(825, 860))
            return True
        return None

    def action_max_time(self):
        time.sleep(0.5)
        max_time = time_consuming(self.steps_basic.verify_zhengbing_max_time())
        logging.info(f'max time: {max_time}')
        self.result.update({
            "time_consuming": max_time
        })
        return True

    def action_click_confirm(self):
        self.device.click(truncated_normal(1325, 1550), truncated_normal(825, 860))
        return True

    def action_click_confirm_end(self):
        if self.steps_basic.verify_click_confirm_end() == '确定':
            self.device.click(truncated_normal(860, 1080), truncated_normal(570, 614))
            return True
        return None

    def execute_draft(self):
        steps = [
            self.action_click,
            self.action_list,
            self.action_zhengbing,
            self.action_zhengbing_max,
            self.action_max_time,
            self.action_click_confirm,
            self.action_click_confirm_end
        ]
        self.execute_steps(steps)

    # -----
    def click_jump_map(self):
        if self.steps_basic.verify_click_jump_map():
            self.device.click(1420, 95)
            return True
        else:
            self.device.click(1428, 104)
            time.sleep(3)
            self.device.click(1420, 95)
            return True

    def click_map_axis(self):
        if self.steps_basic.verify_click_map_axis() == '跳转':
            self.device.click(truncated_normal(1160, 1245), 855)
            time.sleep(1)
            self.device.input(str(self.config['x']), True)
            self.device.click(truncated_normal(200, 1400), truncated_normal(100, 600))
            time.sleep(1)
            self.device.click(truncated_normal(1290, 1360), 855)
            time.sleep(1)
            self.device.input(str(self.config['y']), True)
            self.device.click(truncated_normal(200, 1400), truncated_normal(100, 600))
            time.sleep(1)
            self.device.click(truncated_normal(1410, 1580), truncated_normal(835, 885))
            return True
        return None

    def click_verify_address(self):
        time.sleep(1)
        self.device.click(760, 440)
        address_result = extract_numbers_from_brackets(self.steps_basic.verify_click_address())
        print("address_result:", address_result)
        if address_result is None:
            return False
        if address_result[0] == int(self.config['x']) and address_result[1] == int(self.config['y']):
            return True
        return None

    def execute_search_map(self):
        steps = [
            self.click_jump_map,
            self.click_map_axis,
            self.click_verify_address,
        ]
        self.execute_steps(steps)

    # ----
    def execute_go_map(self):
        axis_result = self.steps_basic.verify_go_map(True)
        if not axis_result:
            return False
        (x, y), v = axis_result
        self.device.click(truncated_normal(x + 550, x + 550 + 150), truncated_normal(y + 200, y + 200 + 30))
        return True

    def execute_operation_go_map(self):
        steps = [
            self.execute_go_map
        ]
        self.execute_steps(steps)

    # ----

    def select_list_action(self):
        distance = self.steps_basic.verify_select_list_action()
        if distance is None:
            return None
        if float(self.config['max_distance']) < float(distance):
            return None
        # 此处还需要有额外的状态 ?
        # axis_results = find_top_template_matches(self.current_screenshot.crop([0, 675, 1600, 850]),
        #                                          ImgNames.get_image(ImgNames.ACTIONLIST))
        # 这一个可能需要多轮重试，ocr不稳定
        list_max = self.steps_basic.verify_process_list()
        print(list_max)
        if len(list_max) == 0:
            return None
        x = list_max[int(self.config['action_list']) - 1][0]
        self.device.click(truncated_normal(x + 212, x + 212 + 60), truncated_normal(650, 800))
        return True

    def action_delay_time(self):
        action_time = self.steps_basic.verify_delay_time()
        if action_time is None:
            # 错误或者重试
            return None
        action_time_result = time_str_to_seconds(action_time)

        if action_time_result == 0:
            # 异常或者错误
            return None
        # 行动的时间
        self.time_sleep = action_time_result
        print('action_time_result: ', action_time_result)
        self.device.click(truncated_normal(1218, 1450), truncated_normal(802, 845))
        return True

    def action_search_map_address(self):
        axis_result = self.steps_basic.verify_search_map_address()
        if not axis_result:
            return False
        (x, y), v = axis_result
        self.map_x = x
        self.map_y = y
        self.device.click(truncated_normal(x + 340 - 20, x + 343), truncated_normal(y + 220, y + 220 + 5))
        return True

    def action_result(self):
        all_state = ['胜', '同归于尽', '胜成功占领', '败', '平']
        next_state = ['胜', '同归于尽', '胜成功占领', '败']
        state_result = self.steps_basic.verify_map_action_result()
        if state_result is None or state_result not in all_state:
            return False
        elif state_result in next_state:
            # 调用返回主页，结束
            self.device.click(1529, 43)
            # 并结束任务执行
            return "TERMINATE"
        else:
            my_remaining_result = self.steps_basic.verify_my_remaining()
            enemy_remaining_result = self.steps_basic.verify_enemy_remaining()
            print('my_remaining', my_remaining_result)
            print('enemy_remaining', enemy_remaining_result)
            if my_remaining_result is None or enemy_remaining_result is None:
                return False
            my_remaining = my_remaining_result.split('/')[0]
            enemy_remaining = enemy_remaining_result.split('/')[0]
            if int(my_remaining) > self.config['my_remaining'] and int(enemy_remaining) < self.config[
                'enemy_remaining']:
                # 等待下一次平局,更新下一次执行时间
                return True
            else:
                self.device.click(1529, 43)
                time.sleep(1)
                return self.action_draw_run()

    def action_draw_run(self):
        self.device.click(self.map_x + 40 + 345, self.map_y - 40 + 230)
        time.sleep(2)
        draw_axis = self.steps_basic.verify_draw_run()
        if draw_axis is None:
            return False
        else:
            (x, y), v = draw_axis
        self.device.click(truncated_normal(1240 + x, 1240 + x + 120), truncated_normal(220 + y, 220 + y + 20))
        return True

    def action_draw_run_time_confirm(self):
        draw_run_time = self.steps_basic.verify_draw_run_time()
        if draw_run_time is None:
            return False
        if time_str_to_seconds(draw_run_time) <= 0:
            return False
        self.time_sleep = int(draw_run_time)
        self.device.click(truncated_normal(1330, 1330 + 150), truncated_normal(808, 808 + 30))
        return True

    def execute_list_action(self):
        steps = [
            self.select_list_action,
            self.action_delay_time
        ]
        self.execute_steps(steps)

    def execute_list_action_result(self):
        steps = [
            self.action_search_map_address,
            self.action_result,
            self.action_draw_run_time_confirm
        ]
        self.execute_steps(steps)

    def execute(self):
        steps_fn = [self.execute_draft, self.execute_search_map, self.execute_operation_go_map,
                    self.execute_list_action, self.execute_search_map, self.execute_list_action_result]
        current_steps = 1
        while current_steps < len(steps_fn):
            fns = steps_fn[current_steps]
            fns()
            while self.time_sleep > 0:
                time.sleep(1)
                self.time_sleep = self.time_sleep - 1
            current_steps = current_steps + 1
        print('出征到撤退')


if __name__ == '__main__':
    capture = Capture(operator=DeviceOperator(DeviceManager('127.0.0.1:16384')),
                      config={"address": "",
                              "x": 646,
                              "y": 966,
                              "num": 3,
                              "action_list": 3,
                              "max_distance": 300,
                              "time_consuming": 0,
                              "my_remaining": 30000,
                              "enemy_remaining": 30000,
                              })
    capture.execute()

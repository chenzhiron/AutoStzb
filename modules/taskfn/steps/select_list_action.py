import numpy as np

from modules.devices.main import DeviceOperator, DeviceManager
from modules.imgs.img_path import ImgNames
from modules.ocr.main import ocr_format_val, ocr_format_list
from modules.taskfn.basic import Basic
from modules.taskfn.tasks_utils import time_str_to_seconds, process_list
from modules.utils import is_template_matched_axis, truncated_normal, find_top_template_matches


class OperationListAction(Basic):

    def select_list_action(self):
        self.current_screenshot = self.device.screenshot()
        distance = ocr_format_val(np.array(self.current_screenshot.crop([1182, 160, 1250, 210])))
        if distance is None:
            return
        if float(self.config['max_distance']) < float(distance):
            return
        # 此处还需要有额外的状态
        axis_results = find_top_template_matches(self.current_screenshot.crop([0, 675, 1600, 850]),
                                                 ImgNames.get_image(ImgNames.ACTIONLIST))
        # 这一个可能需要多轮重试，ocr不稳定
        list_max = process_list(ocr_format_list(np.array(o.current_screenshot.crop([300, 800, 1410, 835]))))
        print(list_max)
        if len(list_max) == 0:
            return
        x = list_max[int(self.config['action_list'])-1][0]
        self.device.click(truncated_normal(x+212, x+212+60), truncated_normal(650,800))
        return True

    def action_delay_time(self):
        self.current_screenshot = self.device.screenshot()
        action_time = ocr_format_val(np.array(self.current_screenshot.crop([770, 650, 883, 690])))
        if action_time is None:
            # 错误或者重试
            return
        action_time_result = time_str_to_seconds(action_time)
        if action_time_result == 0:
            # 异常或者错误
            return
        # 行动的时间
        print(action_time_result)
        self.device.click(truncated_normal(1218, 1450), truncated_normal(802, 845))
        return True

    def action_going(self):
        self.current_screenshot = self.device.screenshot()
        axis_result = is_template_matched_axis(self.current_screenshot.crop([340, 220, 1220, 715]),
                                               ImgNames.get_image(ImgNames.ADDRESS), 0.3)
        print(axis_result)
        if not axis_result:
            return
        (x, y), v = axis_result
        self.device.click(truncated_normal(x + 340, x + 10 + 340), truncated_normal(y + 220, y + 20 + 220))

    def action_result(self):
        self.current_screenshot = self.device.screenshot()

    def execute_list_action(self):
        steps = [
            self.select_list_action,
            self.action_delay_time
        ]
        self.execute_steps(steps)

if __name__ == '__main__':
     o = OperationListAction(DeviceOperator(DeviceManager('127.0.0.1:16384')), {'max_distance':300, 'action_list':4})
     o.execute_list_action()
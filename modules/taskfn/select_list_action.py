import numpy as np
from numpy.f2py.auxfuncs import throw_error

from modules.devices.main import Devices
from modules.imgs.img_path import ImgNames
from modules.taskfn.tasks_utils import BaseReturnMain, time_str_to_seconds
from modules.ocr.main import ocr_format_val
from modules.utils import is_template_matched_axis, truncated_normal, find_top_template_matches


class Operation(BaseReturnMain):
    def __init__(self, device: Devices, config={}, db=None):
        super().__init__(device)
        self.config = {
            "max_distance": '30'
        }
        self.device = device
        self.current_screenshot = None

    def execute(self):
        self.current_screenshot = self.device.screenshot()
        distance =  ocr_format_val(np.array(self.current_screenshot.crop([1182,160,1250,210])))
        if distance is None:
            return
        if float(self.config['max_distance']) < float(distance):
            return
        # 此处还需要有额外的状态
        axis_results = find_top_template_matches(self.current_screenshot.crop([0,675,1600,850]), ImgNames.get_image(ImgNames.ACTIONLIST))
        print(axis_results)
        if not axis_results:
            return
        (x,y), v = axis_results[0]
        self.device.click(truncated_normal(x, x+150), truncated_normal(y+675-120, y+675))

    def action_delay_time(self):
        self.current_screenshot = self.device.screenshot()
        action_time = ocr_format_val(np.array(self.current_screenshot.crop([770,666,895,715])))
        if action_time is None:
            # 错误或者重试
            return
        action_time_result = time_str_to_seconds(action_time)
        if action_time_result == 0:
            # 异常或者错误
            return
        # 行动的时间
        print(action_time_result)
        self.device.click(truncated_normal(1218,1450), truncated_normal(802,845))
    def action_going(self):
        self.current_screenshot = self.device.screenshot()
        axis_result = is_template_matched_axis(self.current_screenshot.crop([340,220,1220,715]), ImgNames.get_image(ImgNames.ADDRESS),0.3)
        print(axis_result)
        if not axis_result:
            return
        (x,y),v = axis_result
        self.device.click(truncated_normal(x+340,x+10+340),  truncated_normal(y+220,y+20+220))

    def action_result(self):
        self.current_screenshot = self.device.screenshot()

if __name__=='__main__':
    d = Devices('127.0.0.1:16384')
    operation = Operation(d)
    operation.action_result()


import time
from typing import Callable, List, Optional

import cv2

from modules.devices.main import DeviceOperator
from modules.imgs.img_path import ImgNames
from modules.utils import is_template_matched_axis


class Basic:
    def __init__(self, device: DeviceOperator, config):
        self.device = device
        self.config = config
        self.result = {}
        self.current_screenshot = None

    def return_main(self):
        return_tag = [ImgNames.get_image(ImgNames.BUILD_RETURN), ImgNames.get_image(ImgNames.BUILD_RETURN2), ImgNames.get_image(ImgNames.LIST_RETURN)]
        while True:
            all_none = True
            screenshot = self.device.screenshot().crop([1200,0,1600,400])
            for v in return_tag:
                result = is_template_matched_axis(screenshot, v)
                if result is not None:
                    (x,y), score = result
                    self.device.click(int(x) + 1200, int(y))
                    all_none = False
                    break
            if all_none:
                break
            time.sleep(1)

    def run_with_retry(self, step_func:Callable, max_retry=20, retry_interval=0.5):
        step_name = step_func.__name__
        for attempt in range(1, max_retry + 1):
            # 执行操作并获取原始结果
            raw_result = step_func()
            if raw_result:
                return raw_result
            print(f"Retry {attempt}/{max_retry} for {step_func.__name__}")
            time.sleep(retry_interval * attempt)  # 递增延迟策略
        print(f"Step {step_name} failed after {max_retry} retries.")
        return False

    def execute_sequence(self,
                         steps: List[Callable],
                         reset_on_failure: bool = True,
                        ):
        """
        增强型顺序步骤执行器
        :param reset_on_failure: True=失败时重置进度，False=从断点继续
        :param steps 步骤
        """
        current_step = 0

        while current_step < len(steps):
            step_func = steps[current_step]
            result = self.run_with_retry(step_func)

            if not result:
                if reset_on_failure:
                    self.return_main()
                    current_step = 0  # 重置进度
                return 'FAILED'

            current_step += 1
        return True

class BaseTypeImg:
    def __init__(self):
        self.attack_template_img = cv2.imread(
            "./modules/imgs/attack_template.png", cv2.IMREAD_COLOR
        )
        self.defense_template_img = cv2.imread(
            "./modules/imgs/defense_template.png", cv2.IMREAD_COLOR
        )
        self.exploit_template_img = cv2.imread(
            "./modules/imgs/condinate.png", cv2.IMREAD_COLOR
        )

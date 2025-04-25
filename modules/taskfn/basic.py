import time

import cv2

from modules.devices.main import DeviceOperator


class Basic:
    def __init__(self, device: DeviceOperator, config):
        self.device = device
        self.config = config
        self.result = {}
        self.current_screenshot = None

    def run_with_retry(self, step_func, max_retry=20, retry_interval=0.5):
            """
            执行一个步骤，支持重试机制
            :param step_func: 要执行的函数（如 self.action_click）
            :param max_retry: 最大重试次数
            :param retry_interval: 重试间隔（秒）
            :return: True 成功，False 失败
            """
            for _ in range(max_retry):
                if step_func():  # 如果返回 True，说明执行成功
                    return True
                time.sleep(retry_interval)
            return False  # 超过最大重试次数仍失败

    def execute_steps(self, steps, max_retry=20, retry_interval=0.5):
            """
            按顺序执行多个步骤
            :param steps: 步骤函数列表（如 [self.action_click, self.action_list]）
            :param max_retry: 每个步骤的最大重试次数
            :param retry_interval: 重试间隔（秒）
            """
            for step in steps:
                step_name = step.__name__
                print(f"Executing step: {step_name}")
                success = self.run_with_retry(step, max_retry, retry_interval)
                if not success:
                    print(f"Step {step_name} failed after {max_retry} retries.")
                    break  # 如果某一步失败，终止整个流程

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


class BaseReturnMain(Basic):
    def return_main(self):
        pass

import cv2

from modules.devices.main import DeviceOperator


class Basic:
    def __init__(self, device: DeviceOperator, config):
        self.device = device
        self.config = config
        self.result = {}
        self.current_screenshot = None


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

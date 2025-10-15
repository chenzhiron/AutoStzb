import time
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
        self.interval_timer = {}

    def return_main(self):
        return_tag = [ImgNames.get_image(ImgNames.BUILD_RETURN), ImgNames.get_image(ImgNames.BUILD_RETURN2),
                      ImgNames.get_image(ImgNames.LIST_RETURN)]
        while True:
            all_none = True
            screenshot = self.device.screenshot().crop([1200, 0, 1600, 400])
            for v in return_tag:
                result = is_template_matched_axis(screenshot, v)
                if result is not None:
                    (x, y), score = result
                    self.device.click(int(x) + 1200, int(y))
                    all_none = False
                    break
            if all_none:
                break
            time.sleep(0.5)
        return True

    def interval_clear(self, event):
        if event in self.interval_timer:
            del self.interval_timer[event]

    def interval_is_reached(self, event, interval=3):
        now = time.time()
        if event in self.interval_timer:
            if now - self.interval_timer[event] < interval:
                return False
        self.interval_timer[event] = now
        return True

    def set_loading_timer(self, key, duration):
        self.interval_timer[key] = time.time() + duration

    def event_with_loading(self, event_fn, interval=2):
        if not self.interval_is_reached(event_fn.__name__, interval):
            return False

        result = event_fn()

        if result:
            self.set_loading_timer(event_fn.__name__, interval)

        return result


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

from modules.devices.main import Devices
from modules.imgs.img_path import ImgNames
from modules.taskfn.tasks_utils import BaseReturnMain
from modules.utils import is_template_matched, is_template_matched_axis, truncated_normal


class Operation(BaseReturnMain):
    def __init__(self, device: Devices, config={}, db=None):
        super().__init__(device)
        self.config = config
        self.device = device
        self.current_screenshot = None

    def execute(self):
        self.current_screenshot = self.device.screenshot()
        axis_result = is_template_matched_axis(self.current_screenshot.crop([550,200,1220,800]), ImgNames.get_image(ImgNames.JINGON))
        if not axis_result:
            return
        (x,y), v = axis_result
        self.device.click(truncated_normal(x+550, x+550+150), truncated_normal(y+200,y+200+30))


if __name__=='__main__':
    d = Devices('127.0.0.1:16384')
    operation = Operation(d)
    operation.execute()


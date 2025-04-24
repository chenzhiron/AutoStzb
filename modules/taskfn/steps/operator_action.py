from modules.imgs.img_path import ImgNames
from modules.taskfn.basic import Basic
from modules.utils import is_template_matched_axis, truncated_normal


class OperationGoMap(Basic):
    def execute_operation_go_map(self):
        self.current_screenshot = self.device.screenshot()
        axis_result = is_template_matched_axis(self.current_screenshot.crop([550, 200, 1220, 800]),
                                               ImgNames.get_image(ImgNames.JINGON))
        if not axis_result:
            return
        (x, y), v = axis_result
        self.device.click(truncated_normal(x + 550, x + 550 + 150), truncated_normal(y + 200, y + 200 + 30))

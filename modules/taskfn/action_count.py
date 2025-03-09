import numpy as np

from modules.ocr.main import ocr_format_val
from modules.utils import (
    find_multiple_templates,
    format_date_strptime,
    pil_to_cv2,
    export_excel,
)
from modules.devices.main import Devices
from modules.taskfn.tasks_utils import BaseTypeImg, battle_time


class ActionCount(BaseTypeImg):
    def __init__(self, d, end_time):
        BaseTypeImg.__init__(self)
        self.d = d
        self.custom_end_time = end_time
        self.result = {}
        self.screenshot = None
        self.filtered_lines = []
        self.end_time = 0
        self.offset_y = 800

    def role_lists(self):
        userdict = {}
        for v in self.filtered_lines:
            username = ocr_format_val(
                np.array(self.screenshot.crop([480, v, 680, v + 50]))
            )
            if username != None:
                userdict.update({username: self.result.get(username, 0) + 1})

        current_end_time = battle_time(self.screenshot, self.filtered_lines[-1])
        if current_end_time != None:
            self.end_time = int(current_end_time)

        return userdict

    def loopinfo(self):
        self.offset_y = 0
        main_img = pil_to_cv2(self.screenshot.crop([40, 0, 100, 600]))
        lines = find_multiple_templates(main_img, self.attack_template_img)
        print("lines:", lines)
        r_lines = []
        for v in lines:
            if v > 560:
                self.offset_y = int(v)
                break
            else:
                r_lines.append(v)
                self.offset_y = int(lines[-1] + 350 - 170)

        self.filtered_lines = r_lines
        print("filtered_lines: ", self.filtered_lines)
        if len(self.filtered_lines) > 0:
            resdict = self.role_lists()
            return resdict
        else:
            return {}

    def execute(self):
        try:
            while True:
                self.screenshot = self.d.screenshot()
                userdict = self.loopinfo()
                print("userdict info_end_time: ", userdict, self.end_time)
                if (
                    self.end_time is not None
                    and self.end_time != 0
                    and self.custom_end_time > self.end_time
                ):
                    break
                self.result.update(userdict)
                print("self.offset_y", self.offset_y)
                self.d.swipe(
                    800,
                    self.offset_y,
                    800,
                    175,
                )
        finally:
            a_r = []
            a_r.append(["姓名", "出击次数"])
            for key, value in self.result.items():
                a_r.append([key, value])

            export_excel(a_r, "出击次数")


if __name__ == "__main__":
    d = Devices("127.0.0.1:16384")
    flip = ActionCount(d, format_date_strptime("2025/3/9 00:00:00"))
    flip.execute()

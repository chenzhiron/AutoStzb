import numpy as np

from modules.devices.main import Devices
from modules.ocr.main import ocr_format_val
from modules.taskfn.tasks_utils import BaseTypeImg
from modules.utils import export_excel, find_multiple_templates, pil_to_cv2


class Honor(BaseTypeImg):
    def __init__(self, d):
        BaseTypeImg.__init__(self)
        self.d = d
        self.honordict = {}
        self.offset_y = 760
        self.screenshot = None
        self.filtered_lines = []
        self.offset_top = 235

    def siege_battles(self):
        datadict = {}
        for v in self.filtered_lines:
            print(v)
            username = ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [124, v + self.offset_top, 300, v + self.offset_top + 60]
                    )
                )
            )
            honornum = ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [560, v + self.offset_top, 740, v + self.offset_top + 60]
                    )
                )
            )
            print("username:", username, "honornum:", honornum)
            if username and honornum:
                datadict[username] = honornum
            else:
                continue

        return datadict

    def loopinfo(self):
        self.offset_y = 0
        main_img = pil_to_cv2(self.screenshot.crop([1080, 235, 1150, 760]))
        lines = find_multiple_templates(
            main_img, self.exploit_template_img, offset_y=20
        )
        self.filtered_lines = lines
        print("filtered_lines: ", self.filtered_lines)
        if len(self.filtered_lines) > 0:
            self.offset_y = int(lines[-1]) + 235
            resdict = self.siege_battles()
            return resdict
        else:
            return {}

    def exportdate(self):
        a_r = []
        a_r.append(["姓名", "武勋"])
        for key, value in self.honordict.items():
            a_r.append([key, value])
        export_excel(a_r, "武勋数据")

    def execute(self):
        while True:
            self.screenshot = self.d.screenshot()
            resdict = self.loopinfo()
            dictlen = len(resdict)
            like = 0
            for v in resdict.keys():
                if self.honordict.get(v) is not None:
                    like += 1
            if like == dictlen:
                break
            self.honordict.update(resdict)
            print("self.offset_y", self.offset_y)
            self.d.swipe(800, self.offset_y, 800, 235 - 90, 2)

        self.exportdate()


if __name__ == "__main__":
    d = Devices("127.0.0.1:16384")
    Honor(d).execute()

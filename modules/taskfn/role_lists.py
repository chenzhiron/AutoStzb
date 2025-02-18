import numpy as np
import sys

sys.path.append("")
from modules.devices.main import Devices
from modules.ocr.main import ocr_format_val
from modules.utils import export_excel, find_multiple_templates, pil_to_cv2
from modules.taskfn.tasks_utils import BaseTypeImg, battle_time


class RoleLists(BaseTypeImg):

    def __init__(self, d, end_time):
        BaseTypeImg.__init__(self)
        self.d = d
        self.custom_end_time = end_time
        self.end_time = 0
        self.result = []
        self.offset_y = 965
        self.screenshot = None
        self.filtered_lines = []

    def siege_battles(self):
        resarr = []

        for v in self.filtered_lines:
            current = []

            isnpc = ocr_format_val(
                np.array(self.screenshot.crop([1084, v + 195, 1308, v + 195 + 60]))
            )
            if isnpc == "守军":
                continue

            maxNumber = ocr_format_val(
                np.array(
                    self.screenshot.crop([1584, v + 185 + 70, 1762, v + 185 + 130])
                )
            ) or ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [1584, v + 185 + 133, 1762, v + 185 + 130 + 130]
                    )
                )
            )
            print("maxNumber", maxNumber)

            if maxNumber is None:
                continue
            try:
                ln = maxNumber.split("/")[1]
                if int(ln) < 10000:
                    continue
            except :
                print('warning: ', maxNumber)
                
            # 名字
            r = ocr_format_val(
                np.array(self.screenshot.crop([1084, v + 195, 1308, v + 195 + 60]))
            ) or ocr_format_val(
                np.array(self.screenshot.crop([1084, v + 195 - 70, 1308, v + 195]))
            )
            current.append(r)

            # 武将名字
            offset_top = 195 + 139 - 19
            offset_bottom = 195 + 261

            leftv = ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [1084, v + offset_top, 1127, v + offset_bottom]
                    )
                )
            ) or ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [1084, v + offset_top - 70, 1127, v + 261 + 139]
                    )
                )
            )
            current.append(leftv)

            centerv = ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [1319, v + offset_top, 1365, v + offset_bottom]
                    )
                )
            ) or ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [1319, v + offset_top - 70, 1365, v + 261 + 139]
                    )
                )
            )
            current.append(centerv)

            rightv = ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [1547, v + offset_top, 1594, v + offset_bottom]
                    )
                )
            ) or ocr_format_val(
                np.array(
                    self.screenshot.crop(
                        [1547, v + offset_top - 70, 1594, v + 261 + 139]
                    )
                )
            )
            current.append(rightv)

            self.end_time = battle_time(self.screenshot, v)
            print("current", current)

            resarr.append(current)
        return resarr

    def loopinfo(self):
        self.offset_y = 0
        main_img = pil_to_cv2(self.screenshot.crop([40, 185, 122, 740]))
        lines = find_multiple_templates(main_img, self.defense_template_img)
        print("lines:", lines)
        r_lines = []
        for v in lines:
            if v > 620:
                self.offset_y = int(v)
                break
            else:
                r_lines.append(v)

        self.offset_y = int(lines[-1] + 360 + 195)

        self.filtered_lines = r_lines
        print("filtered_lines: ", self.filtered_lines)
        if len(self.filtered_lines) > 0:
            resarr = self.siege_battles()
            return resarr
        else:
            return []

    def execute(self): 
        i = 0

        while True:
            last_end_time = self.end_time

            self.screenshot = self.d.screenshot()
            r2 = self.loopinfo()
            print("r2:", r2)
            if self.end_time is not None and self.end_time != 0 and self.custom_end_time > int(self.end_time):
                break

            r2_l = len(r2)

            if len(self.result) > r2_l and r2_l > 0:
                t = 0
                for k_r, v_r in enumerate(r2):
                    if (
                        self.result[-(k_r + 1)][0] == v_r[0]
                        and self.result[-(k_r + 1)][1] == v_r[1]
                        and self.result[-(k_r + 1)][2] == v_r[2]
                        and last_end_time == self.end_time
                    ):
                        t += 1
                if t == r2_l:
                    i+=1
                    if i == 5:
                        i=0
                        print("len is len")
                        break
            for v in r2:
                self.result.append(v)
            print("self.offset_y", self.offset_y)
            self.d.swipe(950, self.offset_y, 950, 225)
            print(self.result)
        seen = set()
        filtered_data = []
        for lst in self.result:
            if None not in lst and tuple(lst) not in seen:
                seen.add(tuple(lst))
                filtered_data.append(lst)

        export_excel(filtered_data, "敌军主力")


if __name__ == "__main__":
    d = Devices("127.0.0.1:16384")
    RoleLists(d, 1735081240).execute()

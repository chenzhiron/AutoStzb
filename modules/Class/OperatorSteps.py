import time

import numpy as np

from device.AutoMation import automation
from ocr.main import ocrDefault
from device.operate import operateTap, operateSwipe


class OperatorSteps:
    getScreenshots = automation.getScreenshots

    def __init__(self, area, txt, x=0, y=0):
        self.x = x
        self.y = y
        self.verify_txt = txt
        self.area = area

    def getImgOcr(self):
        image = self.getScreenshots()
        res = ocrDefault(np.array(image.crop(self.area)))
        return res

    def verifyOcr(self):
        if self.area == 0:
            return True

        res = self.getImgOcr()
        if res[0] is None:
            return False
        result = ''
        for sublist in res:
            for item in sublist:
                result += item[1][0]
        if not (result in self.verify_txt):
            return False
        return True


class ClickOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x, y):
        super().__init__(area, txt)
        self.x = x
        self.y = y

    def applyClick(self, current_lists=1, offset_y=0, status=False):
        if self.verifyOcr() or status:
            if status:
                time.sleep(1)
            operateTap(self.x * current_lists, self.y + offset_y)
            return True
        return False


class SwipeOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, swipe_lists):
        super().__init__(area, txt)
        self.swipe_lists = swipe_lists

    def applySwipe(self):
        if self.verifyOcr():
            for v in self.swipe_lists:
                operateSwipe(v[0], v[1], v[2], v[3])
            return True
        return False


class OriginalOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x, y):
        super().__init__(area, txt)
        self.x = x
        self.y = y

    def applyOriginalClick(self):
        result = self.getImgOcr()
        if bool(result[0]):
            status = False
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    if line[1][0] == self.verify_txt:
                        first_list = line[0]
                        center_point = [sum(coord) / len(coord) for coord in zip(*first_list)]
                        operateTap(self.x + center_point[0], self.y + center_point[1])
                        status = True
                        break
                break
            if status:
                return True
        return False

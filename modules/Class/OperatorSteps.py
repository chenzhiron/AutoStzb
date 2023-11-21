import numpy as np

from device.AutoMation import automation
from modules.utils.main import ocr_reg
from ocr.main import ocrDefault
from device.operate import operateTap as adbOperateTap, operateSwipe as adbOperateSwipe


class OperatorSteps:
    x, y = 0, 0
    getScreenshots = automation.getScreenshots
    operateTap = adbOperateTap
    operateSwipe = adbOperateSwipe
    ocr = ocrDefault
    ocrReg = ocr_reg

    def __init__(self, area, txt, x=0, y=0):
        self.verify_txt = txt
        self.area = area
        if x == 0:
            self.x = (self.area[0] + self.area[2]) / 2
        if y == 0:
            self.y = (self.area[1] + self.area[3]) / 2

    def getImgOcr(self):
        image = self.getScreenshots()
        res = self.ocr(np.array(image.crop(self.area)))
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
    def __init__(self, area, txt, x=0, y=0):
        super(OperatorSteps, self).__init__(area, txt, x, y)

    def applyClick(self, current_lists=1, offset_y=0, status=False):
        if self.verifyOcr() or status:
            self.operateTap(self.x * current_lists, self.y + offset_y)
            return True
        return False


class SwipeOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, swipe_lists):
        super(OperatorSteps, self).__init__(area, txt)
        self.swipe_lists = swipe_lists

    def applySwipe(self):
        if self.verifyOcr():
            for v in self.swipe_lists:
                self.operateSwipe(v[0], v[1], v[2], v[3])
            return True
        return False


class OriginalOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, offset_x=0, offset_y=0):
        super(OperatorSteps, self).__init__(area, txt, offset_x, offset_y)

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
                        self.operateTap(self.x + center_point[0], self.y + center_point[1])
                        status = True
                        break
                break
            if status:
                return True
        return False

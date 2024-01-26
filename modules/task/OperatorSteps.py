import time

import numpy as np
from modules.ocr.main import ocrDefault
from modules.utils.utils import calculate_max_timestamp


class OperatorSteps:
    def __init__(self, area, txt, x=0, y=0):
        self.x = x
        self.y = y
        self.txt = txt
        self.area = area
        self.ocr_txt = None

    def verifyOcr(self, source):
        res = ocrDefault(np.array(source.crop(self.area)))
        print(res, 'res')
        self.ocr_txt = self.ocr_reg(res)
        return self.ocr_txt

    def verifyTxt(self):
        print(self.ocr_txt, 'ocr_txt')
        print(self.txt, 'self.txt')
        if self.txt is None or self.ocr_txt is None:
            return False
        if len(self.ocr_txt) > 0 and self.ocr_txt[0] is None:
            return False
        for v in self.txt:
            if v in self.ocr_txt:
                return True
        return False

    def ocr_reg(self, res):
        if bool(res[0]):
            return [item[1][0] for sublist in res for item in sublist]
        else:
            return None


class EntryOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        device.operateTap(self.x, self.y)
        return True


class VerifyOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        if self.verifyTxt():
            device.operateTap(self.x, self.y)
            print('x', self.x, 'y', self.y)
            return True
        return False


class SwipeOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, swipe_lists, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.swipe_lists = swipe_lists

    def run(self, device, instance):
        if self.verifyTxt():
            device.operateSwipe(self.swipe_lists)
            return True
        return False


class OcrOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, key, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.key = key

    def run(self, device, instance):
        sleep_time = calculate_max_timestamp(self.ocr_txt)
        print(sleep_time, 'sleep_time')
        # instance.changeConfig(self.key, sleep_time)
        return True


# 返回静态页
class OutOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x, y):
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        while 1:
            img = device.getScreenshots()
            self.verifyOcr(img)
            if self.verifyTxt():
                return True
            time.sleep(0.5)


# 出征页面选择 额外编写


# 战报详情，重写整个方法
class InfoOperatorSteps:
    pass

import time

import numpy as np
from modules.ocr.main import ocrDefault
from modules.utils.utils import calculate_max_timestamp, get_current_date


# 方法 run()
# 结果为True 返回格式: {key:value} or {}, 其中 key 为要修改的实例的属性， value 为本次修改的值
# 结果为False 返回 False
class OperatorSteps:
    def __init__(self, area, txt, x=0, y=0):
        self.x = x
        self.y = y
        self.txt = txt
        self.area = area
        self.ocr_txt = None

    def verifyOcr(self, source):
        print(self.area, 'area')
        res = ocrDefault(np.array(source.crop(self.area)))
        print(res, 'res')
        self.ocr_txt = self.ocr_reg(res)
        return self.ocr_txt

    def verifyTxt(self):
        print(self.ocr_txt, 'ocr_txt')
        print(self.txt, 'self.txt')
        if self.ocr_txt == self.txt:
            return True
        return False

    def ocr_reg(self, res):
        if bool(res[0]):
            return [item[1][0] for sublist in res for item in sublist][0]
        else:
            return None


class EntryOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        device.operateTap(self.x, self.y)
        return {
            'next': True
        }


class VerifyOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        if self.verifyTxt():
            device.operateTap(self.x, self.y)
            print('x', self.x, 'y', self.y)
            return {
                'next': True
            }
        return False


class SwipeOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, swipe_lists, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.swipe_lists = swipe_lists

    def run(self, device, instance):
        if self.verifyTxt():
            device.operateSwipe(self.swipe_lists)
            return {
                'next': True
            }
        return False


class OcrOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, key, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.key = key

    def verifyTxt(self):
        if self.ocr_txt is None:
            return False

    def verifyOcr(self, source):
        res = ocrDefault(np.array(source.crop(self.area)))
        self.ocr_txt = self.ocr_reg(res)
        return self.ocr_txt

    def ocr_reg(self, res):
        if bool(res[0]):
            return [item[1][0] for sublist in res for item in sublist]
        else:
            return None

    def run(self, device, instance):
        sleep_time = calculate_max_timestamp(self.ocr_txt)
        return {
            'next': sleep_time != 0,
            self.key: sleep_time
        }


# 返回静态页
class OutOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x, y):
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        while 1:
            img = device.getScreenshots()
            self.verifyOcr(img)
            if self.verifyTxt():
                return {
                    'next': True
                }
            device.operateTap(self.x, self.y)


# 出征/扫荡 额外情况
class InputOperatorSteps(OperatorSteps):
    def __init__(self, input_value, area, txt, x, y):
        self.input_value = input_value
        super().__init__(area, txt, x, y)

    def run(self):
        # 点击后输入 并退出
        pass


class ExtraOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x, y):
        super().__init__(area, txt, x, y)

    # 重写 识别方法
    def run(self):
        # 根据截图区域识别 扫荡跟出征 并加上偏移坐标
        pass


class StatusOcrOperatorSteps(OperatorSteps):
    def __init__(self, key, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.key = key

    def run(self):
        # 查询状态
        pass


class NumberOcrOperatorSteps(OperatorSteps):
    def __init__(self, key, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.key = key

    def run(self):
        # 查询人数
        pass

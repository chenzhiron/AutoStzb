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
        if self.area is None:
            self.ocr_txt = ''
            return self.ocr_txt
        res = ocrDefault(np.array(source.crop(self.area)))
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
        if sleep_time == None:
            return False
        return {
            'next': sleep_time != 0,
            self.key: sleep_time
        }


# 返回静态页
class OutOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x, y):
        super().__init__(area, txt, x, y)

    def run(self, device):
        while 1:
            img = device.getScreenshots()
            self.verifyOcr(img)
            if self.verifyTxt():
                return True
            time.sleep(0.5)
            device.operateTap(self.x, self.y)


# 出征/扫荡 额外情况
class InputOperatorSteps(OperatorSteps):
    def __init__(self, input_value, area, txt, x, y):
        self.input_value = input_value
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        if self.verifyTxt():
            device.operateTap(self.x, self.y)
            time.sleep(0.5)
            print(self.input_value)
            device.operateInput(self.input_value)
            device.operateTap(400, 400)
            return {
                'next': True
            }
        return False

class Land_EntryOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)
    def verifyOcr(self, source):
        self.ocr_txt = ''
        return self.ocr_txt
    def run(self, device, instance):
        time.sleep(5)
        device.operateTap(self.x, self.y)
        return {
            'next': True
        }


class ExtraOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, x, y):
        super().__init__(area, txt, x, y)
        self.offset_x = 0
        self.offset_y = 0
        self.state = False

    # 重写 识别方法
    def verifyOcr(self, source):
        res = ocrDefault(np.array(source.crop(self.area)))
        try:
            processed_data = []
            for item in res[0]:
                points, label_confidence = item
                label, _ = label_confidence
                # Assuming the points are [top_left, top_right, bottom_right, bottom_left]
                left = points[0][0]
                top = points[0][1]
                right = points[2][0]
                bottom = points[2][1]
                processed_item = [left, top, right, bottom, label]
                processed_data.append(processed_item)
            for v in processed_data:
                if v[4] == self.txt:
                    self.offset_x = v[0]
                    self.offset_y = v[1]
                    self.state = True
                    return self.state
        except Exception as e:
            print(e)
            return self.state

    def run(self, device, instance):
        res = device.getScreenshots()
        if not self.verifyOcr(res):
           return False
        device.operateTap(self.offset_x + self.x, self.offset_y + self.y)
        return {
                'next': True
        }


class StatusOcrOperatorSteps(OperatorSteps):
    def __init__(self, area, txt, key, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.key = key

    def run(self, device, instance):
        if self.ocr_txt:
            return {
                self.key: self.ocr_txt,
                "next": True
            }
        return False


class NumberOcrOperatorSteps(OperatorSteps):
    def __init__(self, key, area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)
        self.key = key

    def run(self, device, instance):
        print(self.ocr_txt)
        if self.ocr_txt:
            return {
                self.key: list(map(int, self.ocr_txt.split('/'))),
                "next": True
            }
        return False

class ChetuitOperatorSteps(OperatorSteps):
    def __init__(self,area, txt, x=0, y=0):
        super().__init__(area, txt, x, y)

    def run(self, device, instance):
        sleep_time = calculate_max_timestamp(self.ocr_txt)
        if sleep_time == None:
             return False
        device.operateTap(self.x, self.y)
        return {
            "next": True
        }

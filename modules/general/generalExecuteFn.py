import time

from ocr.main import ocr_txt_verify
from datetime import datetime


def executeFn(fn, *args):
    count = 0
    while 1:
        time.sleep(0.3)
        result = fn()
        print(result)
        if bool(result[0]):
            return bool(result == args[0])
        else:
            count += 1
            if count > 12:
                raise ZeroDivisionError("识别出错了")


def reg_ocr_verify(area, strlen):
    def fn(areas=area, lens=strlen):
        ocr_txt = ocr_txt_verify(areas)
        result = crop_string(ocr_txt, lens)[0]
        print(result)
        return result

    return fn


def executeClickArea(xy):
    x = (xy[0] + xy[2]) / 2
    y = (xy[1] + xy[3]) / 2
    return x, y


def crop_string(strs, length):
    try:
        value = ''.join(strs)
        cropped_result = [value[i:i + length] for i in range(0, len(value), length)]
        return cropped_result
    except:
        print('出错了')
        return [['']]


def calculate_max_timestamp(time_list):
    timestamp_list = []
    for times in time_list:
        try:
            dt = datetime.strptime(times, '%H:%M:%S')
            timestamp = dt.hour * 3600 + dt.minute * 60 + dt.second
            timestamp_list.append(timestamp)
        except Exception as e:
            timestamp_list.append(0)
    return max(timestamp_list)

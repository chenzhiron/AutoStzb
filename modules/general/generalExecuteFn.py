from ocr.main import ocr_txt_verify
from datetime import datetime


def executeFn(fn, *args):
    try:
        result = fn()
        if bool(result[0]):
            return bool(result == args[0])
        else:
            return False
    except Exception as e:
        print(e)


def reg_ocr_verify(area, strlen):
    def fn(areas=area, lens=strlen):
        ocr_txt = ocr_txt_verify(areas)
        result = crop_string(ocr_txt, lens)[0]
        return result

    return fn


def executeClickArea(xy):
    x = xy[0] + xy[2]
    y = xy[1] + xy[3]
    return x, y
    # ocr_txt = ocr_txt_verify((295, 575, 340, 650))
    # result = crop_string(ocr_txt, 2)[0]
    # if result == '势力':
    #     device.click(335, 600)
    # time.sleep(1)


def crop_string(strs, length):
    value = ''.join(strs)
    # cropped_string = value[:length]
    cropped_result = [value[i:i + length] for i in range(0, len(value), length)]
    return cropped_result


def calculate_max_timestamp(time_list):
    timestamp_list = []
    for times in time_list:
        dt = datetime.strptime(times, '%H:%M:%S')
        timestamp = dt.hour * 3600 + dt.minute * 60 + dt.second
        timestamp_list.append(timestamp)
    return max(timestamp_list)

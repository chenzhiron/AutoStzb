import datetime


def get_current_date(add_seconds=1):
    now = datetime.datetime.now()
    future_time = now + datetime.timedelta(seconds=add_seconds)
    return future_time


def calculate_max_timestamp(time_list):
    timestamp_list = []
    for times in time_list:
        try:
            dt = datetime.datetime.strptime(times, '%H:%M:%S')
            timestamp = dt.hour * 3600 + dt.minute * 60 + dt.second
            timestamp_list.append(timestamp)
        except Exception as e:
            timestamp_list.append(0)
    return None if len(timestamp_list) == 0 else max(timestamp_list)


def computedexecuteClickArea(xy):
    x = (xy[0] + xy[2]) / 2
    y = (xy[1] + xy[3]) / 2
    return x, y


def ocr_reg(res):
    if bool(res[0]):
        return [item[1][0] for sublist in res for item in sublist]
    else:
        return []

import datetime


def get_current_date(add_seconds=0):
    # 获取当前日期和时间
    now = datetime.datetime.now()
    delta = datetime.timedelta(seconds=add_seconds)
    now = now + delta
    return {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second
    }


def calculate_max_timestamp(time_list):
    timestamp_list = []
    for times in time_list:
        try:
            dt = datetime.datetime.strptime(times, '%H:%M:%S')
            timestamp = dt.hour * 3600 + dt.minute * 60 + dt.second
            timestamp_list.append(timestamp)
        except Exception as e:
            timestamp_list.append(0)
    return max(timestamp_list)


def computedexecuteClickArea(xy):
    x = (xy[0] + xy[2]) / 2
    y = (xy[1] + xy[3]) / 2
    return x, y

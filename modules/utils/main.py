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

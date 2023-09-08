import time

from datetime import datetime


def reg_time(reg_str):
    # 转换为时间对象
    time_obj = time.strptime(reg_str, '%H:%M:%S')
    # 获取时间秒数
    seconds = time_obj.tm_hour * 3600 + time_obj.tm_min * 60 + time_obj.tm_sec
    return seconds


def reg_time_ymd(reg_str):
    if len(reg_str) == 18:
        reg_str = reg_str[:10] + ' ' + reg_str[10:]
    # 转换为时间对象
    time_obj = datetime.strptime(reg_str, '%Y/%m/%d %H:%M:%S')
    seconds = time_obj.timestamp()
    return seconds


def split_string(string, step):
    return [string[i:i + step] for i in range(0, len(string), step)]

# if __name__ == '__main__':
#     result = reg_time('耗时00:07:30')
#     print(result)
#     # print(seconds)

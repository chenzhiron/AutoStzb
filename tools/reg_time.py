import time


def reg_time(str):
    # 原始字符串
    string = '耗时00:07:30'

    # 去除前面2个字符
    string = string[2:]

    # 转换为时间对象
    time_obj = time.strptime(string, '%H:%M:%S')

    # 获取时间秒数
    seconds = time_obj.tm_hour * 3600 + time_obj.tm_min * 60 + time_obj.tm_sec
    return seconds


if __name__ == '__main__':
    result = reg_time('耗时00:07:30')
    print(result)
    # print(seconds)


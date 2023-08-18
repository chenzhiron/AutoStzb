import time


def reg_time_2em(reg_str):
    # 去除前面2个字符
    string = reg_str[2:]

    # 转换为时间对象
    time_obj = time.strptime(string, '%H:%M:%S')
    # 获取时间秒数
    seconds = time_obj.tm_hour * 3600 + time_obj.tm_min * 60 + time_obj.tm_sec
    return seconds

def reg_time(reg_str):
    # 去除前面2个字符
    string = reg_str

    # 转换为时间对象
    time_obj = time.strptime(string, '%H:%M:%S')
    # 获取时间秒数
    seconds = time_obj.tm_hour * 3600 + time_obj.tm_min * 60 + time_obj.tm_sec
    return seconds

# if __name__ == '__main__':
#     result = reg_time('耗时00:07:30')
#     print(result)
#     # print(seconds)


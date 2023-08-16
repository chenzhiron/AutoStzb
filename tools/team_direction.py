const_w = 1600
const_h = 900


# 高750

def chuzheng_direction(i):
    w = 1600 - (200 * 2)
    h = 900 - 150
    curr_w = w / 5
    i_w = curr_w * i - 50
    return i_w + 200, h


# 高345
# 宽

def zhengbing_direction(i):
    w = 1600 - 75 - 500
    h = 900 - 555
    curr_w = w / 5
    i_w = curr_w * i - 50
    return i_w, h

import math
from functools import partial


def calculate_distance(base_x, base_y, x, y):
    distance = math.sqrt((x - base_x) ** 2 + (y - base_y) ** 2)
    return distance


# 传入基点坐标，返回要比较的坐标函数
def base_point(x, y):
    return partial(calculate_distance, x, y)


# if __name__ == '__main__':
#     base_x = 1020
#     base_y = 1200
#
#     distance_calculator = base_point(base_x, base_y)
#     point1_x = 1010
#     point1_y = 1100
#
#     point2_x = 1020
#     point2_y = 1250
#
#     distance1 = distance_calculator(point1_x, point1_y)
#     distance2 = distance_calculator(point2_x, point2_y)
#
#     print("第一个坐标距离基点的距离:", distance1)
#     print("第二个坐标距离基点的距离:", distance2)

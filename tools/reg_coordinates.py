def reg_coor(position_array):
    x = (position_array[0][0] + position_array[1][0]) / 2
    y = (position_array[0][1] + position_array[2][1]) / 2
    return [x,y]







# demo
# if __name__ == '__main__':
#     result = reg_coor([[        560,         566],
#        [        722,         566],
#        [        722,         604],
#        [        560,         604]])
#     print(result)
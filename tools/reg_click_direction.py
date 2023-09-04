def reg_direction(direction=(0, 0, 0, 0)):
    x = (direction[0] + direction[2]) / 2
    y = (direction[1] + direction[3]) / 2
    return [x, y]

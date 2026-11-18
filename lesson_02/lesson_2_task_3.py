import math


def square(side):
    area = side * side
    if side % 1 != 0:
        return math.ceil(area)
    else:
        return area


side = 2.5
result = square(side)

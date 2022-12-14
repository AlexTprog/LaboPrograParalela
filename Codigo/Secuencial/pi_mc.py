from multiprocessing import Pool
from random import random

points_total = 100000000  # cien millones


def random_number(index):
    x = random()
    y = random()
    inside = 0
    if x*x + y*y < 1.0:
        inside += 1
    return inside


if __name__ == "__main__":
    point_inside = 0
    pool = Pool()
    result = pool.map(random_number, range(1, points_total))
    for x in result:
        point_inside += x
    print(4.0*point_inside/points_total)

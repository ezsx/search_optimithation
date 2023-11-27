import numpy as np


def griewank_function(x):
    # part1 = 1 + sum(x ** 2) / 4000
    part1 = 1 + sum([x[i] ** 2 for i in range(len(x))]) / 4000
    part2 = 1
    for i in range(len(x)):
        part2 *= np.cos(x[i] / np.sqrt(i + 1))
    return part1 - part2

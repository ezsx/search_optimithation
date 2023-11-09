import numpy as np

random_points = np.random.uniform(-5, 5, (30, 2))
print(random_points)

Points_arr = [
    random_points,
    np.vstack([np.array([0., 0.]), np.array([-1., -1.]), np.array([1., 1.])]),
    [np.array([1., 1.]),np.array([1., 0.])],
    [np.array([3., 3.]), np.array([-3., -3.]), np.array([2., -2.])],
]


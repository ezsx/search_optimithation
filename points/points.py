import numpy as np

random_points = np.random.uniform(-5, 5, (15, 2))

Points_dict = {
    "Random Points": random_points,
    "Points set 1": np.vstack([np.array([0., 0.]), np.array([-1., -1.]), np.array([1., 1.])]),
    "Points set 2": [np.array([1., 1.]), np.array([1., 0.])],
    "Points set 3": [np.array([3., 3.]), np.array([-3., -3.]), np.array([2., -2.])],
}



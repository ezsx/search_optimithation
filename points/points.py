import numpy as np

random_points = np.random.uniform(-5, 5, (30, 2))

points = [
    random_points,
    np.vstack([np.array([0., 0.]), np.array([-1., -1.]), np.array([1., 1.])]),
    [np.array([1., 1.]), np.array([1., 0.])],
    [np.array([3., 3.]), np.array([-3., -3.]), np.array([2., -2.])],
]

Points_dict = {
    f"Random Points ({len(random_points)} pth)": random_points,
    "Points set 1 (3 pth)": np.vstack([np.array([0., 0.]), np.array([-1., -1.]), np.array([1., 1.])]),
    "Points set 2 (2 pth)": [np.array([1., 1.]), np.array([1., 0.])],
    "Points set 3 (3 pth)": [np.array([3., 3.]), np.array([-3., -3.]), np.array([2., -2.])],
}

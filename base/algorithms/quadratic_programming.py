from scipy.optimize import minimize
import numpy as np
from base.algorithms.base_algorithm import BaseAlgorithm


class QuadraticProgramming(BaseAlgorithm):
    def solve(self):
        paths = []
        for point in self.points:
            search_range_1 = (-3, 3)
            search_range_2 = (-3, 3)
            bounds = (search_range_1, search_range_2)
            constraints = {'type': 'eq', 'fun': self.function}

            path = [point]

            def callback(x):
                path.append(x)

            res = minimize(
                self.function,
                point,
                method="SLSQP",
                # bounds=bounds,
                constraints=constraints,
                callback=callback,
                options={'disp': True}
            )
            path.append(res.x)
            paths.append(np.array(path))
        return paths

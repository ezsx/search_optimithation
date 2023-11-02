from scipy.optimize import minimize
import numpy as np
from base.algorithms.base_algorithm import BaseAlgorithm


class QuadraticProgramming(BaseAlgorithm):
    def solve(self):
        search_range = (0, float("inf"))
        bounds = (search_range, search_range)
        constraints = {'type': 'eq', 'fun': self.function}

        paths = []
        for point in self.points:
            path = [point]

            def callback(x):
                path.append(x)

            res = minimize(
                self.function,
                point,
                method="SLSQP",
                bounds=bounds,
                constraints=constraints,
                callback=callback,
                options={'disp': True}
            )
            path.append(res.x)
            paths.append(np.array(path))
        return paths

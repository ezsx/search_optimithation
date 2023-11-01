from scipy.optimize import minimize
import numpy as np
from base.algorithms.base_algorithm import BaseAlgorithm


class QuadraticProgramming(BaseAlgorithm):
    def solve(self, iterations=20):

        b = (0, float("inf"))  # search range
        bounds = (b, b)
        con = {'type': 'eq', 'fun': self.function}

        paths = []
        for point in self.points:
            path = []
            for i in range(iterations):
                def callback(x):
                    g_list = np.ndarray.tolist(x)
                    g_list.append(self.function(x))
                    path.append(g_list)

                res = minimize(self.function, point, method="SLSQP", bounds=bounds,
                               constraints=con, callback=callback)
                glist = np.ndarray.tolist(res.x)
                glist.append(res.fun)
                path.append(glist)
            paths.append(np.array(path))
        return paths

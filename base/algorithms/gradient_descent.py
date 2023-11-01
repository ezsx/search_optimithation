import autograd.numpy as np
from autograd import grad
from base.algorithms.base_algorithm import BaseAlgorithm


class GradientDescent(BaseAlgorithm):
    def solve(self, step=0.01, iterations=20):
        paths = []
        grad_func = grad(self.function)
        for point in self.points:
            path = [point]
            for i in range(iterations):
                gradient = grad_func(point)
                point = point - step * gradient
                path.append(point)
            paths.append(np.array(path))
        return paths

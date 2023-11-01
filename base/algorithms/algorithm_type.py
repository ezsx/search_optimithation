from enum import Enum
from base.algorithms.base_algorithm import BaseAlgorithm
from base.algorithms.gradient_descent import GradientDescent
from base.algorithms.quadratic_programming import QuadraticProgramming


class AlgorithmType(Enum):
    gradient_descent = 'gradient_descent'
    quadratic_programming = 'quadratic_programming'

    def get_algorithm(self, function, points) -> BaseAlgorithm:
        if self == AlgorithmType.gradient_descent:
            return GradientDescent(function, points)
        elif self == AlgorithmType.quadratic_programming:
            return QuadraticProgramming(function, points)

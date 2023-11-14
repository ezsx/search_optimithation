def rosenbrock(X):
    return sum([100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2 for x1, x2 in zip(X[:-1], X[1:])])

import autograd.numpy as np


# Gradient Descent
def Gradient_descent(function, points, learning_rate=0.01, num_iterations=20):
    from autograd import grad
    paths = []
    grad_func = grad(function)
    for x_init in points:
        x = x_init
        path = [x]
        for i in range(num_iterations):
            grad = grad_func(x)
            x = x - learning_rate * grad
            path.append(x)
        paths.append(np.array(path))
    return paths

def gradient_descent(function, points, learning_rate=0.01, num_iterations=20):
    """
        Performs gradient descent optimization on a given function.

        Parameters:
        function (Callable): The function to be minimized.
        points (Array-like): Initial points in the domain of the function from which the gradient descent will start.
        learning_rate (float, optional): Determines the step size at each iteration of the gradient descent algorithm. Defaults to 0.01.
        num_iterations (int, optional): Number of iterations the gradient descent algorithm will perform. Defaults to 20.

        Returns:
        List[Array]: A list of arrays representing the paths taken by the gradient descent algorithm from the initial points.
    """
    import autograd.numpy as np
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

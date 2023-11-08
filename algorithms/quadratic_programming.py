def quadratic_programming(function, points):
    """
    Performs sequential quadratic programming optimization on a given function.

    :parameter
    ----------
    function (Callable): The function to be minimized.
    points (Array-like): Initial points in the domain of the function from which the sequential quadratic programming will start.

    :return
    -------
    List[Array]: A list of arrays representing the paths taken by the sequential quadratic programming from the initial points.
    List[str]: A list of strings representing the output of the sequential quadratic programming at each iteration.
    """
    from scipy.optimize import minimize
    import numpy as np
    from utils.output import rez_output
    paths = []
    output = []
    for point in points:
        # search_range_1 = (-3, 3)
        # search_range_2 = (-3, 3)
        # bounds = (search_range_1, search_range_2)
        constraints = {'type': 'eq', 'fun': function}
        path = [point]

        def callback(x):
            path.append(x)
            # output.append(f'x,y,z = {x[0]:.2f}, {x[1]:.2f}, {function(x):.2f}')

        res = minimize(
            function,
            point,
            method="SLSQP",
            # bounds=bounds,
            constraints=constraints,
            callback=callback,
            options={'disp': True}
        )
        path.append(res.x)
        paths.append(np.array(path))
        output.append(
            rez_output(point, res.x, function)
        )
    return paths, output

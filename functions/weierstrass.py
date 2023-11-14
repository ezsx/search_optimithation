import numpy as np


def weierstrass(x, a=0.5, b=3, n_terms=20):
    """
    Weierstrass function, non-differentiable but continuous.

    :param x: Input value or array.
    :param a: Parameter 'a', with 0 < a < 1.
    :param b: Parameter 'b', a positive odd integer where ab > 1 + (3/2)π.
    :param n_terms: Number of terms in the series to approximate the function.
    :return: Calculated value of the Weierstrass function.
    """
    n = np.arange(n_terms)
    return np.sum(a**n * np.cos(b**n * np.pi * x), axis=0)
import numpy as np


def schwefel_function(x):
    return 418.9829 * len(x) - sum(x * np.sin(np.sqrt(np.abs(x))))

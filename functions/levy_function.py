import numpy as np

def levy_function(x):
    x = np.array(x)  # Ensure x is a NumPy array for element-wise operations
    w = 1 + (x - 1) / 4
    term1 = np.sin(np.pi * w[0])**2
    term3 = (w[-1] - 1)**2 * (1 + np.sin(2 * np.pi * w[-1])**2)
    sum_term = np.sum((w[:-1] - 1)**2 * (1 + 10 * np.sin(np.pi * w[:-1] + 1)**2))
    return term1 + sum_term + term3

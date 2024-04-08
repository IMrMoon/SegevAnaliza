import numpy as np
from colors import bcolors


def romberg_integration(func, a, b, n):
    counter = 1
    """
    Romberg Integration

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of iterations (higher value leads to better accuracy).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    h = b - a
    R = np.zeros((20, 20), dtype=float)

    R[0, 0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, 20):
        h /= 2
        sum_term = 0
        counter += 1
        for k in range(1, 2 ** i, 2):
            sum_term += func(a + k * h)

        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_term

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4 ** j) - 1)

        if np.round(R[i - 1, i - 1], n) == np.round(R[i, i], n):
            print(counter)
            return round(R[i, i], 5)

    print("we have reach maximum iterations {20}")
    return R[19, 19]


def f(x):
    return ((2*x + (np.cos(x**3 + 2*x**2 - 6))) / (x + (2 * np.exp(-2*x))))

# Date: 8.4.24
# Group members:
# Segev Chen 322433400
# Gad Gadi Hasson 207898123
# Carmel Dor 316015882
# Artiom Bondar 332692730
# Git:https://github.com/IMrMoon/SegevAnaliza.git
# Name: Segev Chen
if __name__ == '__main__':

    a = -0.62
    b = 3
    n = 5
    integral = romberg_integration(f, a, b, n)

    print( f" Division into n={n} sections ")
    print(bcolors.OKBLUE, f"Approximate integral in range [{a},{b}] is {integral}", bcolors.ENDC)

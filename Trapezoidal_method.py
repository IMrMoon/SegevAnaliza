
from colors import bcolors
import numpy as np


def trapezoidal_rule(f, a, b, n):
    if a > b:
        a, b = b, a
    h = (b - a) / n
    T = f(a) + f(b)
    integral = ((b-a) * T) / 2  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


if __name__ == '__main__':
    f = lambda x: (np.sin(x**2 + 5*x + 6) / (2 * np.exp(-x)))
    result = trapezoidal_rule(f, 2.1, 2.6, 4000)
    print(bcolors.OKBLUE, "Approximate integral:", result, bcolors.ENDC)

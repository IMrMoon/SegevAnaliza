from colors import bcolors


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


# Date: 8.4.24
# Group members:
# Segev Chen 322433400
# Gad Gadi Hasson 207898123
# Carmel Dor 316015882
# Artiom Bondar 332692730
# Git:https://github.com/IMrMoon/SegevAnaliza.git
# Name: Segev Chen
if __name__ == '__main__':
    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [1.2, 2.3, -0.5, -0.89, -1.37]
    x_interpolate1 = 1.25  # The x-value where you want to interpolate
    x_interpolate2 = 1.55
    y_interpolate1 = lagrange_interpolation(x_data, y_data, x_interpolate1)
    y_interpolate2 = lagrange_interpolation(x_data, y_data, x_interpolate2)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x_interpolate1, "is y =", y_interpolate1, bcolors.ENDC)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x_interpolate2, "is y =", y_interpolate2, bcolors.ENDC)

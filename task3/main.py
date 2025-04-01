import numpy as np
import matplotlib.pyplot as plt
import time
N_MAX = 11


def solution(n, chebyshev=False):
    if chebyshev:
        a, b = (-1, 1)
        xs = np.array([(b + a + (b - a) * np.cos((2 * i + 1) * np.pi / (2 * (n + 1)))) / 2 for i in range(n + 1)])
    else:
        xs = np.array([2 * i / n - 1 for i in range(n + 1)])
    f = 1 / (1 + 25 * xs ** 2)
    y = np.zeros((n + 1, n + 1))
    y[:,0] = f

    for j in range(1, n + 1):
        for i in range(n - j + 1):
            y[i, j] = (y[i + 1, j - 1] - y[i, j - 1]) / (xs[i + j] - xs[i])

    def polynomial(x):
        result = y[0][0]
        product = 1
        for i in range(n):
            product *= x - xs[i]
            result += y[0][i + 1] * product
        return result

    def function(x):
        return 1 / (1 + 25 * x ** 2)

    x_values = np.array(range(-1000, 1000)) * 0.001
    polynomial_values = np.vectorize(polynomial)(x_values)
    f_values = np.vectorize(function)(x_values)
    y_values = np.vectorize(abs)(polynomial_values - f_values)
    plt.scatter(x_values, y_values, c=str(1 - n / N_MAX), linewidths=0.1)
    # чем темнее, тем больше n


for n in range(3, N_MAX):
    solution(n)
plt.show()

plt.cla()

for n in range(3, N_MAX):
    solution(n, True)
plt.show()

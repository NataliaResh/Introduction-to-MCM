import numpy as np
import matplotlib.pyplot as plt

N_MAX = 11


def solution(n):
    xs = np.array([2 * i / n - 1 for i in range(n + 1)])
    f = 1 / (1 + 25 * xs ** 2)
    y = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        y[i][i] = f[i]

    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            y[i][j] = (y[i + 1][j] - y[i][j - 1]) / (xs[j] - xs[i])

    def polynomial(x):
        result = y[0][0]
        for i in range(n):
            temp = 0
            for j in range(i + 1, n + 1):
                temp += y[0][j]
            result += temp * (x - xs[i])
        return result

    def function(x):
        return 1 / (1 + 25 * x ** 2)

    x_values = np.array(range(-1000, 1000)) * 0.001
    polynomial_values = np.vectorize(polynomial)(x_values)
    f_values = np.vectorize(function)(x_values)
    y_value = np.vectorize(abs)(polynomial_values - f_values)
    plt.scatter(x_values, y_value, c=str(1 - n / N_MAX), linewidths=0.1)
    # чем темнее, тем больше n


n = 3
for n in range(3, N_MAX):
    solution(n)
plt.show()

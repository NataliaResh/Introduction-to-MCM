import numpy as np
import matplotlib.pyplot as plt


def function(y0_type=0, y0=0, yn_type=0, yn=0, n=100):
    if y0_type == yn_type == 1:
        raise ValueError("Граничные условия не должны быть только производными")
    a = -np.pi / 2
    b = np.pi / 2
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    f = np.cos(x)

    A = np.ones(n + 1)
    B = -2 * np.ones(n + 1)
    C = np.ones(n + 1)
    D = h ** 2 * f
    d1 = D[1]
    dn = D[n]
    A[0] = 0
    C[-1] = 0

    if y0_type == 0:
        D[1] -= y0

        D[0] = y0
    elif y0_type == 1:
        B[1] = -1
        D[1] += y0 * h
        print()

    if yn_type == 0:
        D[-2] -= yn
        D[-1] = yn
    elif yn_type == 1:
        B[-2] = -1
        D[-2] -= yn * h

    C[1] = C[1] / B[1]
    D[1] = D[1] / B[1]

    for i in range(2, n):
        denominator = B[i] - A[i] * C[i - 1]
        if i < n - 1:
            C[i] = C[i] / denominator
        D[i] = (D[i] - A[i] * D[i - 1]) / denominator

    for i in range(n - 2, 0, -1):
        D[i] = D[i] - C[i] * D[i + 1]

    if y0_type == 1:
        D[0] = d1 + 2 * D[1] - D[2]

    if yn_type == 1:
        D[-1] = dn + 2 * D[-3] - D[-2]

    return x, D


def f(x, c1, c2):
    return -np.cos(x) + c1 * x + c2 * np.ones(len(x))


def find_max_diff(f, D):
    return max(abs(f - D))


def find_approximation(n=100):
    x1, D1 = function(0, 0, 0, 0, n=n)
    f1 = f(x1, 0, 0)
    epsilon1 = find_max_diff(f1, D1)

    x2, D2 = function(0, 0, 0, 0, n=n * 2)
    f2 = f(x2, 0, 0)
    epsilon2 = find_max_diff(f2, D2)

    return np.log2(epsilon1 / epsilon2)


print("Порядок аппроксимации:", find_approximation())

x, D = function()
plt.plot(x, D)
plt.grid()
plt.show()

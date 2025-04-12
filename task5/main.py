import numpy as np
import matplotlib.pyplot as plt


def solve_poisson(y0_type=0, y0=0, yn_type=1, yn=2, n=100):
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

    plt.plot(x, D)
    plt.grid()
    plt.show()


solve_poisson()

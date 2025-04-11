import numpy as np
import matplotlib.pyplot as plt


def solve_poisson(y0_type=1, y0=1, yn_type=0, yn=0, n=100):
    if (y0_type == yn_type == 1):
        raise ValueError("Граничные условия не должны быть только производными")
    a = -np.pi / 2
    b = np.pi / 2
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    f = np.cos(x)

    A = np.ones(n + 1)
    B = -2 * np.ones(n + 1)
    C = np.ones(n)
    D = h ** 2 * f

    A[0] = 0
    A[-1] = 0
    C[0] = 0
    C[-1] = 0

    if y0_type == 0:
        B[0] = 1
        D[0] = y0
    elif y0_type == 1:
        B[0] = -1 / h
        C[0] = 1 / h
        D[0] = y0 / h

    if yn_type == 0:
        B[-1] = 1
        D[-1] = yn
    elif yn_type == 1:
        A[-1] = -1 / h
        B[-1] = 1 / h
        D[-1] = yn

    C[0] = C[0] / B[0]
    D[0] = D[0] / B[0]

    for i in range(1, n + 1):
        denominator = B[i] - A[i] * C[i - 1]
        if i < n:
            C[i] = C[i] / denominator
        D[i] = (D[i] - A[i] * D[i - 1]) / denominator

    # Обратный ход
    for i in range(n - 1, -1, -1):
        D[i] = D[i] - C[i] * D[i + 1]

    plt.plot(x, D)
    plt.grid()
    plt.show()


solve_poisson()

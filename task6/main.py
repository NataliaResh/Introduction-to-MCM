import numpy as np
import matplotlib.pyplot as plt


def max_diff(f1, f2):
    return max(abs(f1 - f2))


def order_approximation(calculated, calculated_x2, reference, reference_x2):
    epsilon1 = max_diff(calculated, reference)
    epsilon2 = max_diff(calculated_x2, reference_x2)
    return np.log2(epsilon1 / epsilon2)


def newton_polynomial(x, y):
    n = x.size - 1
    table = np.array(y, dtype=float)
    for j in range(1, n + 1):
        for i in range(n, j - 1, -1):
            table[i] = (table[i] - table[i - 1]) / (x[i] - x[i - j])

    def polynomial(t):
        result = table[-1]
        for i in range(n - 1, -1, -1):
            result = result * (t - x[i]) + table[i]
        return result

    return polynomial


def explicit_euler_method(function, a, b, n, ya):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = np.zeros(n + 1)
    y[0] = ya
    for i in range(n):
        y[i + 1] = y[i] + h * function(x[i], y[i])
    return y
    # return newton_polynomial(x, y)


def implicit_euler_method(function, a, b, n, ya):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = np.zeros(n + 1)
    y[0] = ya
    for i in range(n):
        y[i + 1] = y[i] + h * function(x[i] + h, y[i] + h)
    return y


def rk4(function, a, b, n, ya):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = np.zeros(n + 1)
    y[0] = ya
    for i in range(n):
        k1 = function(x[i], y[i])
        k2 = function(x[i] + h / 2, y[i] + h * k1 / 2)
        k3 = function(x[i] + h / 2, y[i] + h * k2 / 2)
        k4 = function(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y


def f1(x, y):
    return np.cos(x)


solution1 = lambda x: np.sin(x) + np.sin(1)

a = -1
b = 1
n = 100
x_values = np.linspace(a, b, n + 1)
x_values_x2 = np.linspace(a, b, n * 2 + 1)
y_values = explicit_euler_method(f1, a, b, n, 0)
y_values_x2 = explicit_euler_method(f1, a, b, n * 2, 0)
print("Порядок аппроцсимации явного метода Эйлера:",
      order_approximation(y_values, y_values_x2, solution1(x_values), solution1(x_values_x2)))
plt.plot(x_values, y_values)
plt.grid()
plt.show()

plt.cla()

x_values = np.linspace(a, b, n + 1)
y_values = implicit_euler_method(f1, a, b, n, 0)
y_values_x2 = implicit_euler_method(f1, a, b, n * 2, 0)
print("Порядок аппроцсимации неявного метода Эйлера:",
      order_approximation(y_values, y_values_x2, solution1(x_values), solution1(x_values_x2)))
plt.plot(x_values, y_values)
plt.grid()
plt.show()

plt.cla()

x_values = np.linspace(a, b, n + 1)
y_values = rk4(f1, a, b, n, 0)
y_values_x2 = rk4(f1, a, b, n * 2, 0)
print("Порядок аппроцсимации метода Рунге-Кутта четвертого порядка:",
      order_approximation(y_values, y_values_x2, solution1(x_values), solution1(x_values_x2)))
plt.plot(x_values, y_values)
plt.grid()
plt.show()


def function2(x, u, v):
    return (998 * u + 1998 * v, -999 * u - 1999 * v)


def solution2(x):
    u = 2 * np.exp(-x - 1) - np.exp(1000 * x - 1000)
    v = np.exp(-1000 * x - 1000) - np.exp(-x - 1)
    return u, v


def explicit_euler_method_2(function, a, b, n, ua, va):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    u = np.zeros(n + 1)
    v = np.zeros(n + 1)
    u[0] = ua
    v[0] = va
    for i in range(n):
        fi = function(x[i], u[i], v[i])
        u[i + 1] = u[i] + h * fi[0]
        v[i + 1] = v[i] + h * fi[1]
    return u, v


a = -1
b = 1
n = 100
x_values = np.linspace(a, b, n + 1)
u_values, v_values = explicit_euler_method_2(function2, a, b, n, 0, 0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, u_values, v_values)
plt.grid()
plt.show()


def implicit_euler_method_2(function, a, b, n, ua, va):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    u = np.zeros(n + 1)
    v = np.zeros(n + 1)
    u[0] = ua
    v[0] = va
    for i in range(n):
        fi = function(x[i] + h, u[i] + h, v[i] + h)
        u[i + 1] = u[i] + h * fi[0]
        v[i + 1] = v[i] + h * fi[1]
    return u, v


a = -1
b = 1
n = 100
x_values = np.linspace(a, b, n + 1)
u_values, v_values = implicit_euler_method_2(function2, a, b, n, 0, 0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, u_values, v_values)
plt.grid()
plt.show()

r = 0.3


def function3(x, y, z, t):
    return (10 * (y - x),
            x * (r - z) - y,
            x * y - 8 / 3 * z)


def rk4_3(function, a, b, n, xa, ya, za):
    t = np.linspace(a, b, n + 1)
    h = (b - a) / n
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)
    x[0] = xa
    y[0] = ya
    z[0] = za
    for i in range(n):
        k1 = function(x[i], y[i], z[i], t[i])
        k2 = function(x[i] + h * k1[0] / 2, y[i] + h * k1[1] / 2, z[i] + h * k1[2] / 2, t[i] + h / 2)
        k3 = function(x[i] + h * k2[0] / 2, y[i] + h * k2[1] / 2, z[i] + h * k2[2] / 2, t[i] + h / 2)
        k4 = function(x[i] + h * k3[0], y[i] + h * k3[1], z[i] + h * k3[2], t[i] + h)
        x[i + 1] = x[i] + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        y[i + 1] = y[i] + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        z[i + 1] = z[i] + h / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
    return x, y, z


r = 24.06
a = -10
b = 10
n = 1000
t_values = np.linspace(a, b, n + 1)
x_values, y_values, z_values = rk4_3(function3, a, b, n, 3.051522, 1.582542, 15.62388)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print(z_values)
ax.scatter(x_values, y_values, z_values)
plt.grid()
plt.show()

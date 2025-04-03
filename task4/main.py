from numpy import sin, pi, e, log2
from scipy import integrate


def f1(x):
    return sin(pi * x ** 5) / (x ** 5 * (1 - x))


def f2(x):
    return e ** (-(x ** 0.5) + sin(x / 10))


def fourth_central_difference(f, x, h=1e-5):
    return (f(x - 2 * h) - 4 * f(x - h) + 6 * f(x) - 4 * f(x + h) + f(x + 2 * h)) / (h ** 4)


def simpson_formula(function, a, b, n):
    if n % 2 != 0:
        n += 1
    if b == float("inf"):
        new_f = lambda x: function(x / (1 - x)) / ((1 - x) ** 2)
        b = 1
    else:
        new_f = lambda x: function(x)
    e = 1e-10
    a += e
    b -= e
    h = (b - a) / n
    result = 0
    for i in range(1, n, 2):
        result += (new_f(a + (i - 1) * h) + 4 * new_f(a + i * h) + new_f(a + (i + 1) * h)) * h / 3

    m4 = 0
    t = a
    for _ in range(n):
        m4 = max(m4, abs(fourth_central_difference(new_f, t)))
        t += h
    error = (b - a) * h ** 4 * m4 / 180
    return result, error


def foo(function, a, b, n=None):
    print("-" * 100)
    if n is None:
        n = int(input("Количество разбиений = "))
    else:
        print("Количество разбиений =", n)
    real_result, real_error = integrate.quad(function, a, b)
    simpson_result, simpson_error = simpson_formula(function, a, b, n)
    epsilon = abs(real_result - simpson_result)

    simpson_result_x2, simpson_error_x2 = simpson_formula(function, a, b, n * 2)
    epsilon_x2 = abs(real_result - simpson_result_x2)

    print("Реальное значение =", real_result, "+-", real_error)
    print("Значение методом Симпсона =", simpson_result)
    print("Максимальная погрешность =", simpson_error)
    print("Разница =", epsilon)
    print("Порядок аппроксимации? =", log2(epsilon / epsilon_x2))


foo(f1, 0, 1, n=250)
print()
foo(f2, 0, float("inf"), n=50000)

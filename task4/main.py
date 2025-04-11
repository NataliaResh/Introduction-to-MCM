from numpy import sin, pi, e
from math import log

def f1(x):
    if x == 0:
        return pi
    if x == 1:
        return pi * 5
    return sin(pi * x ** 5) / (x ** 5 * (1 - x))

def f2(x):
    if x == float("inf"):
        return 0
    return e ** (-(x ** 0.5) + sin(x / 10))


def fourth_central_difference(f, x, h=1e-5):
    return (f(x - 2 * h) - 4 * f(x - h) + 6 * f(x) - 4 * f(x + h) + f(x + 2 * h)) / (h ** 4)


def simpson_formula(function, a, b, n):
    if n % 2 != 0:
        n += 1
    if b == float("inf"):
        def new_f(x):
            if x == 1:
                return function(float("inf"))
            return function(x / (1 - x)) / ((1 - x) ** 2)
        b = 1
    else:
        new_f = lambda x: function(x)
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


def foo(function, a, b, real_result, n=None):
    print("-" * 100)
    if n is None:
        n = int(input("Количество разбиений = "))
    else:
        print("Количество разбиений =", n)

    simpson_result, simpson_error = simpson_formula(function, a, b, n)
    simpson_result_x2, simpson_error_x2 = simpson_formula(function, a, b, n * 2)
    simpson_result_x4, simpson_error_x4 = simpson_formula(function, a, b, n * 4)

    epsilon = abs(simpson_result_x2 - simpson_result)
    epsilon_x4 = abs(simpson_result_x2 - simpson_result_x4)

    print("Реальное значение =", real_result)
    print("Значение методом Симпсона =", simpson_result)
    print("Максимальная погрешность =", simpson_error)
    print("Разница =", abs(simpson_result - real_result))
    print("Порядок аппроксимации? =", log(epsilon / epsilon_x4, 2))


foo(f1, 0, 1, 8.034910675416853, n=1000)
print()
foo(f2, 0, float("inf"), 2.981003452558113, n=50000)

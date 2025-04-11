import numpy as np
from scipy.integrate import quad

# Функция 1: сингулярность на концах
def f1(x):
    if x == 0 or x == 1:
        return 0  # избегаем деления на 0 (будет обработано интегратором)
    return np.sin(np.pi * x ** 5) / (x ** 5 * (1 - x))


# Функция 2: бесконечный предел
def f2(x):
    return np.exp(-np.sqrt(x) + np.sin(x / 10))


# Метод Симпсона (с оценкой точности и порядком сходимости)
def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1  # n должно быть чётным
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = h / 3 * (y[0] + 2 * np.sum(y[2:n:2]) + 4 * np.sum(y[1:n:2]) + y[n])
    return S


# Приближение бесконечного интеграла заменой предела
def f2_transform(t):
    # x = t / (1 - t) => t in [0, 1) maps to x in [0, ∞)
    x = t / (1 - t)
    jacobian = 1 / (1 - t) ** 2
    return f2(x) * jacobian


def simpson_order():
    # Исследование порядка аппроксимации на простом примере
    exact = 2.0  # Интеграл x^2 от 0 до sqrt(3) = 2
    f = lambda x: x ** 2
    a, b = 0, np.sqrt(3)
    errors = []
    ns = [10, 20, 40, 80, 160]
    for n in ns:
        approx = simpsons_rule(f, a, b, n)
        errors.append(abs(approx - exact))
    rates = [np.log(errors[i - 1] / errors[i]) / np.log(2) for i in range(1, len(errors))]
    print("Порядок аппроксимации метода Симпсона:")
    for i, rate in enumerate(rates, 1):
        print(f"n = {ns[i]}: порядок ≈ {rate:.2f}")


print("Вычисление интегралов с точностью 1e-8:\n")

# Интеграл 1: от 0 до 1
print("Интеграл 1: ∫₀¹ sin(πx⁵)/(x⁵(1-x)) dx")
result1, err1 = quad(f1, 0, 1, epsabs=1e-10, epsrel=1e-10, limit=100)
print(f"Результат: {result1:.10f}, Оценка погрешности: {err1:.1e}")
print(simpsons_rule(f1, 0, 1, 100))
# Интеграл 2: от 0 до ∞ (замена переменной)
print("\nИнтеграл 2: ∫₀^∞ exp(-√x + sin(x/10)) dx")
result2, err2 = quad(f2_transform, 0, 1, epsabs=1e-10, epsrel=1e-10)
print(f"Результат: {result2:.10f}, Оценка погрешности: {err2:.1e}")

# Исследование порядка аппроксимации
print("\nПроверка порядка аппроксимации на примере ∫₀^{√3} x² dx")
simpson_order()

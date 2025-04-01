import numpy as np
import matplotlib.pyplot as plt

e = 1e-10

def f(z):
    return z ** 3 - 1

def f_(z):
    return 3 * z * z

    
def newtons_method(x):
    if x == 0:
        return 0
    x1 = x - f(x) / f_(x)
    while abs(x1 - x) > e:
        x = x1
        x1 = x - f(x) / f_(x)
    return x1

def real(x):
    return x.real

def img(x):
    return x.imag

array = np.array([complex(i * 0.1, j * 0.1) for i in range(-30, 30) for j in range(-30, 30)])

answer_array = np.vectorize(newtons_method)(array)

answer1 = np.fromiter((array[i] for i in range(len(array)) if abs(answer_array[i] - complex(1, 0)) < 1e-5),
                      dtype= array.dtype)
answer2 = np.fromiter((array[i] for i in range(len(array)) if abs(answer_array[i] - complex(-0.5, 0.86603)) < 1e-5),
                      dtype= array.dtype)
answer3 = np.fromiter((array[i] for i in range(len(array)) if abs(answer_array[i] - complex(-0.5, -0.86603)) < 1e-5),
                      dtype= array.dtype)

plt.scatter(np.vectorize(real)(answer1), np.vectorize(img)(answer1), color='orange')
plt.scatter(1, 0, c='red')
plt.scatter(np.vectorize(real)(answer2), np.vectorize(img)(answer2), color='yellow')
plt.scatter(-0.5, 0.86603, c='gold')
plt.scatter(np.vectorize(real)(answer3), np.vectorize(img)(answer3), color='green')
plt.scatter(-0.5, -0.86603, c='darkgreen')
plt.show()

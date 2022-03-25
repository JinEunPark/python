import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = 2 * x + 3
y2 = x ** 2 - 2 * x + 4
graph1, = plt.plot(x, y)
graph2, = plt.plot(x, y2)
plt.legend(handles=(graph1, graph2), labels=(r'$graph1$', r'$graph2'))
plt.show()

x = np.log(7) / np.log(4)
y3 = (2 ** x - 2 ** (-x)) / (2 ** x + 2 ** (-x))  # 괄호 신경 쓸것
print(y3)

x1 = np.linspace(-2, 4, 400)
y3 = ((0.5) ** (x1 + 1)) - 3
plt.plot(x1, y3)
plt.show()

x2 = np.linspace(1, 100, 1000)
y9 = np.zeros_like(x2)


def g(x):
    return np.log(x) / np.log(3)


def f(x):
    return x ** 2 - 4 * x + 3


for i in range(0, 1000):
    y9[i] = f(g(x2[i]))

g1 = plt.plot(x2, y9)
plt.legend(handles=(g1), labels=(r'$y=f(g(x))$'))
plt.show()

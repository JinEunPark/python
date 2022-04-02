import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x)


def T1(x):
    return x


def T2(x):
    return T1(x) - (1 / 6) * x ** 3


def T3(x):
    return T2(x) + (1 / 120) * x ** 5


def T4(x):
    return T3(x) + (1 / 5040) * x ** 7


x = np.linspace(-np.pi, np.pi, 1001)
y = f(x)
y2 = T1(x)
y3 = T2(x)
y4 = T3(x)
y5 = T4(x)

graph1, = plt.plot(x, y)
graph2, = plt.plot(x, y2)
graph3, = plt.plot(x, y3)
graph4, = plt.plot(x, y4)
graph5, = plt.plot(x, y5)
plt.legend(handles=(graph1, graph2, graph3, graph4, graph5),
           labels=('$y=sin(x)$', '$y=T_1(x) $', '$y=T_2(x)$', '$y=T_3(x)$', '$y=T_4(x)$'))
plt.show()

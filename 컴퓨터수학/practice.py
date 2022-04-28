import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-(1 / 2) * np.pi, (1 / 2) * np.pi, 1000)
x2 = np.linspace(-(1 / 2) * np.pi, (1 / 2) * np.pi, 1000)
x3 = np.linspace(-(1 / 2) * np.pi, (1 / 2) * np.pi, 1000)
x4 = np.linspace(-(1 / 2) * np.pi, (1 / 2) * np.pi, 1000)
x5 = np.linspace(-(1 / 2) * np.pi, (1 / 2) * np.pi, 1000)

y = np.zeros_like(x)
y2 = np.zeros_like(x)
y3 = np.zeros_like(x)
y4 = np.zeros_like(x)
y5 = np.sin(x)


def T(x):
    return x


def T2(x):
    return T(x) - (1 / 6) * x ** 3


def T3(x):
    return T2(x) + (1 / 120) * x ** 5


def T4(x):
    return T3(x) - (1 / 5040) * x ** 7


for i in range(1000):
    y[i] = T(x[i])
    y2[i] = T2(x2[i])
    y3[i] = T3(x3[i])
    y4[i] = T4(x4[i])

graph1, = plt.plot(x, y)
graph2, = plt.plot(x2, y2)
graph3, = plt.plot(x3, y3)
graph4, = plt.plot(x3, y3)
graph5, = plt.plot(x5, y5)
plt.legend(handles=(graph1, graph2, graph3, graph4, graph5), labels=('T', 'T2', 'T3', 'T4', 'sinx'))
plt.show()

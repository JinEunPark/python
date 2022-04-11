import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)
y = np.zeros_like(x)


def f(x):
    if np.abs(x) < 1:
        return 0
    elif np.abs(x) > 1:
        return x
    elif x == 1:
        return 0.5
    elif x == -1:
        return -0.5


for i in range(len(x)):
    y[i] = f(x[i])

plt.plot(x, y, '.')
plt.show()

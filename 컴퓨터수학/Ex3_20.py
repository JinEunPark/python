import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(3, 5, 201)
fx = x ** 2 + 1
x1 = 4
fx1 = x1 ** 2 + 1
plt.scatter(x1, fx1)
plt.plot(x, fx, 'b')
plt.show()

x3 = np.linspace(-6, -5 - 0.015, 101)
x4 = -5
x5 = np.linspace(-5 + 0.015, -4, 101)

gx1 = (x3 ** 2 - 25) / (x3 + 5)
gx2 = -10
gx3 = (x5 ** 2 - 25) / (x5 + 5)

plt.plot(x3, gx1, 'k')
plt.plot(x5, gx3, 'k')
plt.plot(x4, gx2, 'o', mfc='none')
plt.show()

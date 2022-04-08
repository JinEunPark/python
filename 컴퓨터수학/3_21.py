import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 10, 10000)
fx = 1 / x
plt.plot(x, fx)
plt.show()

x2 = np.linspace(-10, 10, 1000)
fx2 = x2 ** 3 + 2 * x2
plt.plot(x2, fx2)
plt.show()

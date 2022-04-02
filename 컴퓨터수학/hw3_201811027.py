import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 1000, 10000)
y = (np.log(x) / np.log(3)) ** 2 - (np.log(x ** 4) / np.log(3)) + 3
plt.plot(x, y)
plt.show()

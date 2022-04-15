import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol('x')
fx = (2 * x - 1) ** 4
print("f'(x)=", sp.diff(fx, x))

fx2 = 1 / (x - x ** 3)
print("2f'(x)=", sp.diff(fx2, x))

fx3 = sp.log(sp.tan(x))
print("3f'(x)=", sp.diff(fx3, x))

fx4 = sp.exp(x ** (1 / 2))
print("f'(x)=", sp.diff(fx4, x))

x1 = np.linspace(-5, 5, 1000)
fx = np.exp(-x1 ** 2)
graph1, = plt.plot(x1, fx)

x2 = np.linspace(0.001, 10, 100)
fx2 = x2 ** (2 / 3)
graph2, = plt.plot(x2, fx2)
plt.legend(handles=(graph1, graph2), labels=(r'$np.exp(-x1 ** 2)&', r'$x ** (2 / 3)$'))
plt.show()

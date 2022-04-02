import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.1, 4, 401)
y1 = np.log2(x1)
x2 = np.linspace(0.9, 4, 501)
y2 = np.log2(x2 + 1) - 1
graph1, = plt.plot(x1, y1)
graph2, = plt.plot(x2, y2)
plt.legend(handles=(graph2, graph2), labels=(r'$y = log_2(x)', r'$y = log_2(x+1)-1'))
plt.show()

x3 = np.linspace(-1, np.pi - 1, 501)
y3 = np.sin(2 * (x3 + 1))
x4 = np.linspace(0, 2 * np.pi, 501)
y4 = -3 * np.cos(x4) + 1
graph3, = plt.plot(x3, y3)
graph4, = plt.plot(x4, y4)
plt.legend(handles=(graph3, graph4), labels=(r'$y = sind2(x+1)$', r'$y=-3cos(x+1)$'))
plt.show()

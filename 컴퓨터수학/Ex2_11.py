import matplotlib.pyplot as plt
import numpy as np

ang1deg = 60
ang1rad = np.deg2rad(ang1deg)
print("60도는 =", ang1rad)

ang2rad = -3 / 2 * np.pi
ang2rad = np.rad2deg(ang2rad)
print("-3/2PI=", ang2rad)

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(2 * (x + 1))
y2 = 3 * np.cos(x) + 1
graph7, = plt.plot(x, y)
graph8, = plt.plot(x, y2)
plt.legend(handles=(graph7, graph8), labels=(r'$y=sin(2(x+1)$', r'$y=cos(x)+1$'))
plt.show()

z = np.linspace(-0.25 * np.pi, 0.25 * np.pi, 501)
y3 = np.tan(2 * (z - 0.5 * np.pi))
plt.plot(z[10:491], y3[10:491])
plt.show()

x1 = np.linspace(-10, 10, 1000)
y4 = 1 / (1 + np.e ** (-x1))
plt.plot(x1, y4)
plt.show()

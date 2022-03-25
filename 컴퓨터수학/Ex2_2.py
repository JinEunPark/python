import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,1000)
y = (x+1)**2 -1
plt.plot(x,y)
plt.show()

x2 = np.linspace(0,10,1000)
y2 = -1/2*(x-1)**2 +2
plt.plot(x2,y2)
plt.show()

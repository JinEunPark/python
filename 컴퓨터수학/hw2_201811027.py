import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
fx = np.zeros_like(x)  # 정의역과 같은 크기의 0 리스트 생성


def f(x):
    if x <= -1:
        return x + 2
    elif x > -1:
        return x ** 2


for i in range(0, 1000):
    fx[i] = f(x[i])

plt.plot(x,fx)
plt.show()

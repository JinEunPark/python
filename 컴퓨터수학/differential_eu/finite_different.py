import matplotlib.pyplot as plt
import numpy as np


def dpf(F, x, h):  # 내부에서 실행할 함수, 변수 x, limt 0으로 갈 변수 h 전진차분법
    return (F(x + h) - F(x)) / h


def d0f(F, x, h):  # 중앙차분법
    return (F(x + h) - F(x - h)) / (2 * h)


def dmf(F, x, h):  # 후진 차분법
    return (F(x) - F(x - h)) / h


def f(x):
    return np.exp(x)


list_dpf = []
list_d0f = []
list_dmf = []
list_h = []
a = 2  # f'(2)에서 값을 비교하기 위해서 사용
df = 4 * np.exp(4)
for i in range(11):
    h = (1.0 / 2.0) ** i
    list_h.append(h)
    list_dpf.append(np.abs(f(a) - dpf(f, a, h)))
    list_d0f.append(np.abs(f(a) - d0f(f, a, h)))
    list_dmf.append(np.abs(f(a) - dmf(f, a, h)))
graph1, = plt.loglog(list_h, list_dpf, 'o-')
graph2, = plt.loglog(list_h, list_d0f, 'o-')
graph3, = plt.loglog(list_h, list_dmf, 'o-')
plt.legend(handles=(graph1, graph2, graph3),
           labels=(r'$(f(a+h)-f(x))/h$', r'$(f(x-h)-f(x+h))/2h$', r'$(f(x-h)-f(x))/h$'),
           loc='lower right')
plt.show()

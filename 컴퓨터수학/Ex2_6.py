import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 2000)
y = 3 ** x
y2 = 3 ** (x - 1) + 2
graph1, = plt.plot(x, y)
graph2, = plt.plot(x, y2)  #
plt.legend(handles=(graph1, graph2), labels=(r'$3^x$', r'$3^{x-1}+2$'))
plt.show()
# handles = 에 아규먼트로 그래프 객체 전달, labels 에 범례전달.


x1 = np.linspace(-5, 5, 1000)
y3 = (0.5) ** x1
y4 = -(0.5) ** (x1 + 2)
graph3, = plt.plot(x1, y3)
graph4, = plt.plot(x1, y4)
plt.legend(handles=(graph3, graph4), labels=(r'$0.5^x$', r'$-0.5^{x+2}$'))
plt.show()

x3 = np.linspace(0.1, 4, 1000)
y5 = np.log2(x3)
x4 = np.linspace(-0.9, 4, 1000)
y6 = np.log2(x4 + 1) - 1
graph5, = plt.plot(x3, y5)
graph6, = plt.plot(x4, y6)
plt.legend(handles=(graph5, graph6), labels=(r'$y=log_2(x)$', r'$y=log_2(x+1)-1$'))
plt.show()
# 그래프 한번에 여러개 플롯할 때 꼭 , 직는거 잊지 ㅁ라자 진은아 이거 안직으면 복잡해진다.
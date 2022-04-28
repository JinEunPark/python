# def even():
#     n = int(input("정수를 입력하세요"))
#     list = [i for i in range(n + 1) if i % 2 == 0]
#     return list
#
#
# print(even())

# x = np.linspace(1, 10, 1000)
# fx = 3 * x + 1
# gx = np.sqrt(x - 1)# 진은아 항상 0보다 커야한다잉 알겠니
#
# graph1, = plt.plot(x, fx)
# graph2, = plt.plot(x, gx)
# plt.legend(handles=(graph1, graph2), labels=('1', '2'))
# plt.show()

# def fx(x):
#     return x ** 3 + 1
#
#
# def gx(x):
#     return np.sqrt(x + 2)
#
#
# print(gx(fx(2)))
# print(fx(gx(2)))
# print(gx(gx(2)))

# def f(x):
#     if -1 <= x < 1:
#         return -x ** 2 + 2
#
#     if 1 <= x <= 3:
#         return x ** 2 + 8 * x - 14
#
#     if 3 < x <= 5:
#         return -x ** 2 + 8 * x - 14
#
#
# x = np.linspace(-10, 10, 1000)
# y = np.zeros_like(x)
# for i in range(len(x)):
#     y[i] = f(x[i])
# plt.plot(x, y,'.')
# plt.show()
# def fx(x):
#     if x <= -1:
#         return x + 2
#     if x > -1:
#         return x ** 2
#
#
# x = np.linspace(-10, 10, 1000)
# y = np.zeros_like(x)
# for i in range(len(x)):
#     y[i] = fx(x[i])
# plt.plot(x, y)
# # plt.show()
# x = np.linspace(-np.pi, np.pi)
# fx = np.sin(2 * (x + 1))
# gx = -3 * np.cos(x) + 1
# plt.plot(x, fx)
# plt.plot(x, gx)
# plt.show()

# sum = 0
# for i in range(1, 11):
#     sum += i ** 2 - i
# print(sum)
# sum = 0
# for i in range(1, 6):
#     sum += i ** 3 + 3 * i
# print(sum)
# n = 10
# sum = n * (n + 1) * (2 * n + 1) / 6 - n * (n + 1) / 2
# print(sum)
# n = 5
# sum2 = ((n * (n + 1)) / 2) ** 2 + 3 * (n * (n + 1) / 2)
# print(sum2)
#
# n_list = []
# an_list = []
#
# a1 = 109
# an = a1
# an_list.append(a1)
# n_list.append(1)
# anp1 = 0
#
# for n in range(1000000):
#     if an % 2 == 0:
#         anp1 = an / 2
#     else:
#         anp1 = 3 * an + 1
#     an_list.append(anp1)
#     n_list.append(n + 1)
#     if anp1 == 1:
#         print("n=", n+1)
#         break
#     an = anp1
# plt.plot(n_list, an_list,'-o')
# plt.show()
#
#
# print(10000*(1.03)**10)
# sum = 0
# for i in range(20):
#     sum = (sum +100000)*(1.03)
# print(sum)
# x = np.linspace(0.01, 110, 1000)
# fx = (np.log(x) / np.log(3)) ** 2 - (np.log(x ** 4) / np.log(3) ) + 3
# plt.plot(x, fx)
# plt.show()
# plt.plot
# np.linsace()

# x = np.linspace(0, 4 - 0.15, 1000)
# fx = x ** 2 + 1
# x1 = 4
# f1 = 17
# plt.plot(x, fx, 'k', x1, f1, 'o')
# plt.show()

# x = np.linspace(-6, -5 - 0.015, 101)  # -5 전까지 범위 설정
# x2 = np.linspace(-5 + 0.015, -4, 101)
# fx = (x ** 2 - 25) / (x + 5)
# fx1 = (x2 ** 2 - 25) / (x2 + 5)
# x1 = -5
# f1 = -10
# plt.plot(x, fx, 'k', x2, fx1, 'k')
# plt.plot(x1, f1, 'o', mfc='none')
# plt.show()
# x = np.linspace(-2, -0.015, 100)
# x2 = np.linspace(0.015, 10000, 100000)
# fx = 1 / x
# fx2 = 1 / x2
# plt.plot(x, fx, 'k', x2, fx2)
# plt.show()
# c = 2.5
#
# for n in range(1, 100):
#     if (1 + c) ** n < 1 + n * c:
#         print("the given statement is False")
# print("(1+c)^n >= 1 + n*c")
#
# x = np.linspace(-3, 3, 1000)
# y = np.zeros_like(x)

# def fx(x):
#     if np.abs(x) < 1:
#         return 0
#     if np.abs(x) > 1:
#         return x
#     if x == 1:
#         return 0.5
#     if x == -1:
#         return -0.5
#
#
# for i in range(len(x)):
#     y[i] = fx(x[i])
# plt.plot(x, y, '.')
# plt.show()

# x = sp.Symbol('x')
# fx = x ** 3 - 2 * x ** 2 + 1
# # print(sp.diff(fx, x), "\n", sp.diff(sp.diff(fx, x)), "\n", sp.diff(sp.diff(sp.diff(fx, x))))
# x = sp.Symbol('x') # 변수 x 를 문자로 사용한다고 선언
# gx = sp.sin(x) + sp.exp(x)
# print(sp.diff(gx, x, 3))
# x = sp.Symbol('x')
# fx = (x**2 +2)**3
# print(sp.diff(fx,x))
# gx = 1/(x**4 + 1)**2
# print(sp.diff(gx))
# x = sp.Symbol('x')
# fx = sp.log(x**2 +4)
# print(sp.diff(fx,x))
# x = sp.Symbol('x')
# gx = sp.sin(sp.tan(x))
# print(sp.simplify(sp.diff(gx)))
# import numpy as np
#
#
# def dpf(f, x, h):
#     return (f(x + h) - f(x)) / h
#
#
# def d0f(f, x, h):
#     return (f(x + h) - f(x - h)) / (2 * h)
#
#
# def dmf(f, x, h):
#     return (f(x - h) - f(x)) / h
#
#
# def df(x):
#     return np.exp(x ** 2) * 2 * x
#
#
# def f(x):
#     return np.exp(x ** 2)
#
#
# listDpf = []
# listD0f = []
# listDmf = []
# Alist = []
#
# for i in range(11):
#     a = (1 / 2) ** i
#     listDpf.append(np.abs(dpf(f, 2, a) - df(2)))
#     listD0f.append(np.abs(d0f(f, 2, a) - df(2)))
#     listDmf.append(np.abs(dmf(f, 2, a) - df(2)))
#     Alist.append(a)
#
# g1, = plt.loglog(Alist, listDpf, '-o')
# g2, = plt.loglog(Alist, listDmf, '-o')
# g3, = plt.loglog(Alist, listD0f, '-o')
# # plt.show()
# a1 = 1
# an = a1
# anp1 = 0
# for i in range(1, 3):
#     anp1 = an / (2 * an + 1)
#     an = anp1
# print(anp1)

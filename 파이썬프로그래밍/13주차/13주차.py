import numpy as np
import sympy as sp

a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
if (np.dot((a + b), c) == np.dot(a, c) + np.dot(b, c)):
    print("np.dot((a+b),c):", np.dot((a + b), c), "=", "np.dot(a,c)+np.dot(b,c):", np.dot(a, c) + np.dot(b, c))

k = 30
if (np.dot((k * a), b) == np.dot(a, (k * b))):
    print("np.dot((k*a),b):", np.dot((k * a), b), "=", "np.dot(a,(k*b)):", np.dot(a, (k * b)))

x = sp.Symbol('x')
t = sp.Symbol('t')
fx = (sp.exp(x * 2)) / (sp.exp(x) + 1)
ft = 1 / (sp.exp(t) + 1)
fx1 = sp.Abs(sp.sin(x))
fx2 = x * sp.sqrt(x ** 2 + 2)
fx3 = sp.exp(x) * sp.sin(x)
print("the answer is :", sp.integrate(fx, (x, 0, 2)) - sp.integrate(ft, (t, 0, 2)))
print("the answer is :", sp.integrate(fx1, (x, -sp.pi, sp.pi)))
print("the answer is :", sp.integrate(fx2, (x, 1, 3)))
print("the anserr is :", sp.integrate(fx3, (x, 0, sp.pi / 2)))

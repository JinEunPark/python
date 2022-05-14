import sympy as sp

# a
x = sp.Symbol('x')
t = sp.Symbol('t')
fx = sp.exp(2 * x) / (sp.exp(x) + 1)
tx = 1 / (sp.exp(t) + 1)
print("result", sp.integrate(fx, (x, 0, 2)) - sp.integrate(tx, (t, 0, 2)))
# b
fx2 = sp.Abs(sp.sin(x))
print("result2", sp.integrate(fx2, (x, -sp.pi, sp.pi)))
# c
fx3 = x * sp.sqrt(x ** 2 + 2)
print("result3", sp.integrate(fx3, (x, 1, 3)))
# d
fx4 = sp.exp(x) * sp.sin(x)
print("result4", sp.integrate(fx4, (x, 0, sp.pi / 2)))

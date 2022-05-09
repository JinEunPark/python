import sympy as sp

x = sp.Symbol('x')
fx = 1 / (x * (x + 1))
print("Fx = ", sp.integrate(fx, x))
fx2 = (2 * x - 3) / (x ** 2 - 3 * x + 2)
print("Fx2= ", sp.integrate(fx2, x))

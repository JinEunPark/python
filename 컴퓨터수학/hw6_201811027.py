import sympy as sp

x, k = sp.symbols('x k')
fx = sp.exp(2 * x) * sp.sin(3 * x)
fxd = sp.diff(fx)
fxd2 = sp.diff(fxd)
equation = fxd2 + k * fxd + 13 * fx
print(sp.solve(equation, k, dict=True))

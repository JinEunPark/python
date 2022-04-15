import sympy as sp
import numpy as np

x = sp.Symbol('x')
fx = x ** 2020 + 3 * x ** 3 - 1
print("f'(x)=", sp.diff(fx, x))

fx2 = x / (x + 1)
print("f'(x)=", sp.diff(fx2, x))


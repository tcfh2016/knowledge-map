import sympy as sy

x = sy.Symbol('x')
print(sy.solve(x**2 - 1))
print(sy.solve(x**2 - 1 - 3))
print(sy.solve(x**3 + 0.5*x**2 - 1))

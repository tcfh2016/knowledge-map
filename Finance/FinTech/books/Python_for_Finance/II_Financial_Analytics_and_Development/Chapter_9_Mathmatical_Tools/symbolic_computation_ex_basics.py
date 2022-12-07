import sympy as sy

x = sy.Symbol('x')
y = sy.Symbol('y')
print(type(x))
print(3 + sy.sqrt(x) - 4**2)

sy.init_printing(pretty_print=False, use_unicode=False)
f = x**2 + 3 + 0.5*x**2 + 3/2
print(f)
print(sy.simplify(f))
print(sy.pretty(f))

print(sy.pretty(sy.sqrt(x) + 0.5))

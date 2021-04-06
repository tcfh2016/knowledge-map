import sympy as sy

x = sy.Symbol('x')
a = sy.Symbol('a')
b = sy.Symbol('b')
#a, b = sy.Symbol('a, b')
sy.init_printing(pretty_print=False, use_unicode=False)
print (sy.pretty(sy.Integral(sy.sin(x) + 0.5 * x, (x, a, b))))

int_func = sy.integrate(sy.sin(x) + 0.5 * x, x)
print (sy.pretty(int_func))

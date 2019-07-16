# [Integration](https://docs.scipy.org/doc/scipy/reference/integrate.html)

## Integrating functions, given function object

[scipy.integrate.fixed_quad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.fixed_quad.html#scipy.integrate.fixed_quad)

scipy.integrate.fixed_quad(func, a, b, args=(), n=5)[source]

使用固定顺序的高斯正交法求取有限积分。基于函数func，求取a到b区间的高斯正交积分。

```
>>> from scipy import integrate
>>> f = lambda x: x**8
>>> integrate.fixed_quad(f, 0.0, 1.0, n=4)
(0.1110884353741496, None)
>>> integrate.fixed_quad(f, 0.0, 1.0, n=5)
(0.11111111111111102, None)
>>> print(1/9.0)  # analytical result
0.1111111111111111
```

## Integrating functions, given fixed samples

## Solving initial value problems for ODE systems

## Old API

## Solving boundary value problems for ODE systems

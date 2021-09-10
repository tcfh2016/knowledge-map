# [Optimization and Root Finding ](https://docs.scipy.org/doc/scipy/reference/optimize.html#module-scipy.optimize)

SciPy中的optimize模块提供了求取最大值、最小值的功能。

## Scalar Functions Optimization

## Local (Multivariate) Optimization

[minimize(method=’SLSQP’)](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html)

使用顺序最小二乘规划来计算最小值。

## Global Optimization

[scipy.optimize.brute](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brute.html#scipy.optimize.brute)

scipy.optimize.brute(func, ranges, args=(), Ns=20, full_output=0, finish=<function fmin>, disp=False, workers=1)

通过暴力求取函数的最小值。


## Least-squares and Curve Fitting

## Root finding

## Linear Programming

## Utilities

## Legacy Functions

[scipy.optimize.fmin](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html#scipy.optimize.fmin)

scipy.optimize.fmin(func, x0, args=(), xtol=0.0001, ftol=0.0001, maxiter=None, maxfun=None, full_output=0, disp=1, retall=0, callback=None, initial_simplex=None)

寻找最小值。

# [Linear algebra (numpy.linalg)](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

`linalg`是NumPy提供了针对线性代数学计算的函数库。

## Matrix and vector products

## Decompositions

## Matrix eigenvalues

## Norms and other numbers

## Solving equations and inverting matrices

[numpy.linalg.lstsq(a, b, rcond='warn')](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq)

返回线性矩阵算式的最小二乘方。

- a: (M, N) 矩阵
- b: {(M,), (M, K)} 纵坐标
- x: {(N,), (N, K)} 最小二乘方的值。

## [最小二乘法](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98%E6%B3%95)

最小二乘法（英语：least squares method），又称最小平方法，是一种数学优化方法。它通过最
小化误差的平方和寻找数据的最佳函数匹配。

利用最小二乘法可以简便地求得未知的数据，并使得这些求得的数据与实际数据之间误差的平方和为
最小。最小化问题的精度，依赖于所选择的函数模型。

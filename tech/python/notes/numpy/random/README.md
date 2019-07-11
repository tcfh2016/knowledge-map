# [Random sampling (numpy.random)](https://docs.scipy.org/doc/numpy/reference/routines.random.html)

## Simple random data

[numpy.random.rand(d0, d1, ..., dn)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html#numpy.random.rand)

创建给定模型的处于[0,1)的服从均匀分布的随机数。

参考：

- [均匀分布](https://zh.wikipedia.org/wiki/%E9%80%A3%E7%BA%8C%E5%9E%8B%E5%9D%87%E5%8B%BB%E5%88%86%E5%B8%83)

## Permutations

## Distributions

[random.standard_normal(size=None)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.standard_normal.html#numpy.random.standard_normal)

生成符合标准正态分布的随机样本 (mean=0, stdev=1)，返回值为float或者ndarry。

```
>>> s = np.random.standard_normal(8000) #生成包含8000个随机值的一维数组。
>>> s
array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311, #random
       -0.38672696, -0.4685006 ])                               #random
>>> s.shape
(8000,)

np.random.standard_normal(size=(3, 4, 2)) #生成包含3*4*2个随机值的三维数组。
```

## Random generator

[random.seed(seed=None)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html#numpy.random.seed)

设定随机数生成器的种子，随机数生成算法依据第一个初始值（种子）来进行数字随机，不设置的时
候默认以当前时间来生成随机数，因此可以保证随机数的随机性。基于相同种子所生成的实际上是伪
随机序列。

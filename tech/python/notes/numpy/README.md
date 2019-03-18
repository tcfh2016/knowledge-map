## ndarry常用方法

### numpy.round(a, decimals=0, out=None)

统一小数点位数。

### numpy.cumsum(a, axis=None, dtype=None, out=None)[source]

等价于 numpy.ndarray.cumsum，计算累加和。

- 给定a为一维数组时：将当前元素与前一个元素相加再重新写入当前元素。
- 给定a为二维数组时：通过axis指定累加方向。


## random常用方法

### random.seed(seed=None)

设定随机数生成器的种子，随机数生成算法依据第一个初始值（种子）来进行数字随机，不设置的时
候默认以当前时间来生成随机数，因此可以保证随机数的随机性。基于相同种子所生成的实际上是伪
随机序列。

### random.standard_normal(size)

生成符合标准正态分布的随机样本，返回值为float或者ndarry。

```
np.random.standard_normal(8000) #生成包含8000个随机值的一维数组。
np.random.standard_normal(size=(3, 4, 2)) #生成包含3*4*2个随机值的三维数组。
```

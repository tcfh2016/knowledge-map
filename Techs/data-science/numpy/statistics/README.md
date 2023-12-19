## 常用方法

- sum：对数组中某轴或者全部元素求和，零长度的和为0
- mean：算术平均值，零长度的数组平均值为NaN
- std, var：标准差和方法
- min, max：最小值和最大值
- argmin, argmax：最小、最大元素的索引
- cumsum：所有元素的累计和
- cumprod：所有元素的累计积

## 正态分布

```
# 创建d1行d2列的服从标准正态分布的数组，mean=0, variance=1
numpy.random.randn(d1, d2)

# 创建正态分布，loc为均值，scale为标准差
random.normal(loc=0.0, scale=1.0, size=None)

# 生成符合标准正态分布的随机样本 (mean=0, stdev=1)，返回值为float或者ndarry。
random.standard_normal(size=None)
```


参考：

- [numpy.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html)
- [numpy.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
- [numpy.random.standard_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html)


## 均匀分布

```
# 创建d1行d2列的服从`[0, 1)`均匀分布的数组
numpy.random.rand(d1, d2)

# 返回整数的范围为[low, high)且服从离散均匀分布(discrete uniform distribution)的随机数，如果low/high只给定一个参数那么默认为high。
numpy.random.randint(low, high=None, size=None, dtype=np.uint8)

# 返回范围为[0, 1)且服从连续均匀分布(continuous uniform distribution)的随机数
random.random(size=None)

# 返回范围为[low, high)服从连续均匀分布的随机数
random.uniform(low=0.0, high=1.0, size=None)

# 从给定的1-D数组生成均匀分布的随机序列。如果a为数组，直接从其中进行挑选，如果a为整数，会从np.arange(a)进行挑选样本。
numpy.random.choice(a, size=None, replace=True, p=None)
```

- [均匀分布](https://zh.wikipedia.org/wiki/%E9%80%A3%E7%BA%8C%E5%9E%8B%E5%9D%87%E5%8B%BB%E5%88%86%E5%B8%83)
- [numpy.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html)
- [numpy.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html)
- [numpy.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html)
- [numpy.random.choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html)


## Random generator

[random.seed(seed=None)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html#numpy.random.seed)

设定随机数生成器的种子，随机数生成算法依据第一个初始值（种子）来进行数字随机，不设置的时候默认以当前时间来生成随机数，因此可以保证随机数的随机性。基于相同种子所生成的实际上是伪随机序列。

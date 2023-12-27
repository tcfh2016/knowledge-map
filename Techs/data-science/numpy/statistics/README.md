## 统计学常用方法

- `a.sum(axis=None)`：对数组中某轴或者全部元素求和，零长度的和为0。用`sum(a)`按列求和。
- `a.mean(axis=None)`：算术平均值，零长度的数组平均值为NaN
- `a.std(axis=None)`, `a.var(axis=None)`：标准差和方法
- `a.min(axis=None)`, `a.max(axis=None)`：最小值和最大值
- `a.argmin(axis=None)`, `a.argmax(axis=None)`：最小、最大元素的索引
- `a.prod(axis=None)`：求积
- `a.cumsum`：所有元素的累计和
- `a.cumprod`：所有元素的累计积

上面函数中，指定`axis=0`表示按列求和，`axis=1`表示按行求和，`axis=-1`表示按最后一维求和。

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


### [numpy.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False)](https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.std.html#numpy.std)

计算标准差，默认计算整个数组元素，可以指定坐标轴进行计算。

```
>>> a = np.array([[1, 2], [3, 4]])
>>> np.std(a)
1.1180339887498949
>>> np.std(a, axis=0)
array([ 1.,  1.])
>>> np.std(a, axis=1)
array([ 0.5,  0.5])
```

### [numpy.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False)](https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.var.html#numpy.var)

计算方差，默认计算整个数组元素，可以指定坐标轴进行计算。

```
>>> a = np.array([[1,2],[3,4]])
>>> np.var(a)
1.25
>>> np.var(a, axis=0)
array([ 1.,  1.])
>>> np.var(a, axis=1)
array([ 0.25,  0.25])
```


## 数值回归

### [np.polyval(p, x)(https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyval.html)

假设p是一个长度为N的数组，那么`np.polyval(p, x)`返回如下计算式的值：

```
p[0]*x**(N-1) + p[1]*x**(N-2) + ... + p[N-2]*x + p[N-1]
```

参考：

- [多项式计算](https://ww2.mathworks.cn/help/matlab/ref/polyval.html)

举例：

```
>>> np.polyval([3,0,1], 5)  # 3 * 5**2 + 0 * 5**1 + 1
76
```

### [np.polyfit(x, y, deg)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html)

返回阶数为deg的多项式p(x)的系数，该系数是y中数据的最佳拟合（在最小二乘法中），p中系数按降幂排列。

```
 p(x) = p[0] * x**deg + ... + p[deg]
```

初步理解起来，`polyval`和`polyfit`互为逆运算：

- polyval：给定系数p(1,2...N+1)，底数x(1,2...N+1)，幂为 (N...0)，计算出多项式的值为y。
- polyfit: 给定值y(1,2...N+1)，底数x(1,2...N+1)，幂为(N...0)，计算出对应多项式的系数p(1,2...N+1)


举例：

```
>>> x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
>>> y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
>>> z = np.polyfit(x, y, 3)
>>> z
array([ 0.08703704, -0.81349206,  1.69312169, -0.03968254])
```

注：回归分析是一种统计学上分析数据的方法，目的在于了解两个数据或多个数据之间是否相关，相关方向和强度，并建立数学模型以便观察或预测。简单来说，回归分析是建立因变量Y和自变量X之间的关系模型。

参考：

- [多项式曲线拟合](https://ww2.mathworks.cn/help/matlab/ref/polyfit.html)
- [回归分析](https://zh.wikipedia.org/wiki/%E8%BF%B4%E6%AD%B8%E5%88%86%E6%9E%90)


## 数据抽样

### [np.linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)

返回给定区间均衡的抽样值。

```
>>> np.linspace(2.0, 3.0, num=5)
array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
>>> np.linspace(2.0, 3.0, num=5, endpoint=False)
array([ 2. ,  2.2,  2.4,  2.6,  2.8])
>>> np.linspace(2.0, 3.0, num=5, retstep=True)
(array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
```
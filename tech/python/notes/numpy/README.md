# numpy

NumPy 是一个免费的、如同Matlab一样功能强大的数值计算开发平台。

## numpy常用数组计算函数

### [numpy.zeros(shape, dtype=float, order='C')](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)

根据给定的规格和类型返回新的数组，并初始化为0。其中的order表示在存储多维数组的时候是按照
C语言中的行优先还是Fortran语言中的列优先进行。

```
>>> np.zeros(5)
array([ 0.,  0.,  0.,  0.,  0.])

>>> s = (2,2)
>>> np.zeros(s)
array([[ 0.,  0.],
       [ 0.,  0.]])
```

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

返回阶数为deg的多项式p(x)的系数，该系数是y中数据的最佳拟合（在最小二乘法中），p中系数按
降幂排列。

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

注：回归分析是一种统计学上分析数据的方法，目的在于了解两个数据或多个数据之间是否相关，相
关方向和强度，并建立数学模型以便观察或预测。简单来说，回归分析是建立因变量Y和自变量X之间
的关系模型。

参考：

- [多项式曲线拟合](https://ww2.mathworks.cn/help/matlab/ref/polyfit.html)
- [回归分析](https://zh.wikipedia.org/wiki/%E8%BF%B4%E6%AD%B8%E5%88%86%E6%9E%90)

### [np.sin](https://docs.scipy.org/doc/numpy-1.9.3/reference/generated/numpy.sin.html)

sin函数的定义如下:

- 以原点为中心，半径为1的圆。
- 以原点为起点，以+x轴与圆的交叉点为终点画一条线，将这条线绕逆时针进行旋转，定义角度为a。
- 当角度为a时，这条线与圆的交叉点的纵坐标值即为 sin(a)的值。

按照如上定义，所具有值的范围为：

- a 的范围为[0, 360 ray（度）]，也为[0, 2pi]
- sin(a)的值为 [0, 0]是一个周期性波动的值：
  - a = 0ray/ 0pi, sin(a) = 0
  - a = 90ray/ 0.5pi, sin(a) = 1
  - a = 180ray/ 1.0pi, sin(a) = 0
  - a = 270ray/ 1.5pi, sin(a) = -1
  - a = 360ray/ 2.0pi, sin(a) = 0

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

## numpy常用方法

### [np.allclose(np.array(a), np.array(b))](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)

返回两个array是否相等，会逐一比较每个元素，并且允许一定的误差，默认为1e-05。

```
numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)[source]
```

### numpy.round(a, decimals=0, out=None)

统一小数点位数。

### numpy.cumsum(a, axis=None, dtype=None, out=None)[source]

等价于 numpy.ndarray.cumsum，计算累加和。

- 给定a为一维数组时：将当前元素与前一个元素相加再重新写入当前元素。
- 给定a为二维数组时：通过axis指定累加方向。

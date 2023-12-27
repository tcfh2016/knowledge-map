# [Mathematical functions](https://docs.scipy.org/doc/numpy/reference/routines.math.html)

## Trigonometric functions

## Hyperbolic functions

## Rounding


### numpy.round(a, decimals=0, out=None)

统一小数点位数。

### numpy.cumsum(a, axis=None, dtype=None, out=None)[source]

等价于 numpy.ndarray.cumsum，计算累加和。

- 给定a为一维数组时：将当前元素与前一个元素相加再重新写入当前元素。
- 给定a为二维数组时：通过axis指定累加方向。

### [numpy.mean(a, axis=None, dtype=None, out=None, keepdims=False)](https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.mean.html#numpy.mean)

计算指定数据集的算术平均值，支持按照不同坐标轴进行计算。

```
>>> a = np.array([[1, 2], [3, 4]])
>>> np.mean(a)
2.5
>>> np.mean(a, axis=0)
array([ 2.,  3.])
>>> np.mean(a, axis=1)
array([ 1.5,  3.5])
```

## Sums, products, differences

## Exponents and logarithms

### [numpy.exp](https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html#numpy.exp)

`numpy.exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'exp'>`

给所有给定值为幂，以e（近似值2.718281）为底，返回各自的指数值。

### [numpy.log](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log.html#numpy.log)

`numpy.log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'log'>`

计算给定数据集的log值。

参考：

- [numpy.log() in Python](https://www.geeksforgeeks.org/numpy-log-python/)


## Floating point routines

## Rational routines

## Arithmetic operations

## Handling complex numbers

## Miscellaneous

## 三角函数

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

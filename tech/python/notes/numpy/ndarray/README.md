# [The N-dimensional array (ndarray)](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)

ndarry是基于相同类型的多维容器。


# 属性

- ndarray.ndim 	秩，即轴的数量或维度的数量
- ndarray.shape：数组的维度，对于矩阵，n 行 m 列
- ndarray.size：数组元素的总个数，相当于 .shape 中 n*m 的值

# 使用

## 赋值

创建的多维数组，进行赋值的时候会将指定的行或者元素进行统一赋值：

```
# 创建2行3列的numpy.ndarray，然后将首行的所有列值赋值为100。
paths = np.zeros((2, 3), np.float64)
paths[0] = 100
```

# 方法

## [numpy.ndarray.flatten](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html)

返回将多维数组降为一维的数据。

```
>>> a = np.array([[1,2], [3,4]])
>>> a.flatten()
array([1, 2, 3, 4])
```

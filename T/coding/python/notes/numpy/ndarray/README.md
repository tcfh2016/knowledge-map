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

## 选择

Numpy的一维数组和Python的列表类似，区别在于narray的切片是原始视图，这意味着数据不会被复制，任何修改都会直接反应到原数组上。其中的考虑与NumPy用于处理大量数据需要的性能、内存约束有关。

```
arr = np.arange(10)
arr[5:8] = 12
# 输出 array([0,1,2,3,4,12,12,12,8,9])
```

二维数组中索引对应的是一维数组，可以对各个元素进行递归访问。除此之外选择单个元素的时候可以按如下方式进行：

```
arr2d = np.array([[1,2,3], [4,5,6], [7,8,9]])

arr2d[0][2]
arr2d[0,2]
```

使用切片时可以在一个轴或多个轴上进行切片，使用“,”来分隔不同轴上的切片：

```
arr2d[:2, 1:]
arr2d[1,:2]
```


# 方法

## [numpy.ndarray.flatten](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html)

返回将多维数组降为一维的数据。

```
>>> a = np.array([[1,2], [3,4]])
>>> a.flatten()
array([1, 2, 3, 4])
```

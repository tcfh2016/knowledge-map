# `ndarry`

`ndarry`是一个存放相同类型元素的多维容器，每个数组都有一个`shape`表示各个维度大小的元组，和一个`dtype`来说明数组数据的类型的对象。

`ndarry`可以通过`array`函数进行，它接受一切序列型的对象产生对应的NumPy数组。创建的时候可以通过`dtype`参数来指定类型。

- [ndarray]((https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html))


## 属性

- `data.shape`：代表数组维度的元组，比如`(2, 3)`表示数组为2行3列
- `data.size`：数组元素的总个数，相当于 `data.shape`中`2*3`的值
- `data.dtype`：dtype('float64')，即数组元素的类型
- `data.ndim`：秩，即轴的数量或维度的数量


# 数组创建

## 简单数组

创建一维、二维数组，可以直接使用`np.array()`来创建，比如：

```
np.array([1, 2, 3])
np.array([[1, 2, 3], [4, 5, 6]])
```

在创建时可以通过`dtype`参数指定特定类型，NumPy支持比Python更多的类型，比如：

```
np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
```


## 数组复制

通过另外一个数组来创建时，默认`copy = True`。

```
simple_arr2 = np.array(simple_arr1, copy=False)
```


## 便捷创建

- `np.empty([2, 3])` 创建没有任何具体值的数组（初始化随机值）
- `np.zeros([3,4])`：生成3x4元素值为0的数组
- `np.ones([3,4])`：生成3x4元素值为1的数组
- `np.full([3,4], 9)`：生成3x4元素值为9的数组
- `np.arange(0, 90, 10)`：生成等间隔的数组，第3个参数为“步长”
- `np.linspace(0, 90, 10)`：生成等间隔的数组，第3个参数为“个数”
- `np.eye(5)`：生成5x5的对角数组

参考：

- [numpy.zeros(shape, dtype=float, order='C')](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)


## 从已有数据创建

- `np.asarray(a)`：从已有列表、元组创建
- `np.frombuffer(buffer)`：从字符串中创建
- `np.fromiter(iterable)`：从可迭代对象创建
- `np.empty_like(prototype)`：创建与给定数组相同维度和数据类型但未初始化的数组
- `np.zeros_like(prototype)`：创建与给定数组相同维度和数据类型但以0填充的数组
- `np.ones_like(prototype)`：创建与给定数组相同维度和数据类型但以1填充的数组
- `np.ones_like(a, fill_like)`：创建与给定数组相同维度和数据类型但以给定值`fill_like`填充的数组


## 随机数

- `np.random.rand(5)`：随机生成0~1之间的一维数组
- `np.random.rand(2, 5)`：随机生成0~1之间的二位数组
- `np.random.randn(2, 5)`：随机生成满足正态分布的二位数组
- `np.random.randint(low, high, size)`：随机生成一定范围内的随机数
- `np.random.normal(loc, scale, size)`：随机生成均值为loc，标准差为scale的随机数


# 数组选择

- 索引从0开始，比如`arr[0]`代表第一个元素。
- 应用切片，比如`arr[0:2]`选择第前面两个元素。
- 二维数组索引，`arr[0][2]`相当于`arr[0][2]`，代表第1行第3列的值。但使用切片索引的时候需要用`arr[:2, 1:]`。

Numpy的一维数组和Python的列表类似，区别在于narray的切片是原始视图，这意味着数据不会被复制，任何修改都会直接反应到原数组上。其中的考虑与NumPy用于处理大量数据需要的性能、内存约束有关。

1）单元素选择

二维数组中索引对应的是一维数组，可以对各个元素进行递归访问。除此之外选择单个元素的时候可以按如下方式进行：

```
arr2d = np.array([[1,2,3], [4,5,6], [7,8,9]])

arr2d[0][2]
arr2d[0,2]
```

2）批量选择

```
arr = np.arange(10)
arr[5:8] = 12
# 输出 array([0,1,2,3,4,12,12,12,8,9])

# 判断数组中元素大于10的元素赋值为 -10 
a[a > 10] = -10
```

3）使用切片

使用切片时可以在一个轴或多个轴上进行切片，使用“,”来分隔不同轴上的切片：

```
a[:2, 1:]
a[1,:2]
```


# 数组运算

`ndarry`的运算不需要使用循环就能够进行批量运算（矢量化）。

- 大小相等的ndarray之间的任何算术运算都会将运算应用到元素级：`arr1 * arr2`，或者`np.multiply(arr1, arr2)`。
- ndarray与标量的算术运算会将对应标量的运算广播到所有元素：`arr * 3`。
- 大小不同的ndarray之间也会进行广播。

*注：“标量”就是一个单独的数，“向量”是一组数，可以理解为数组。*


## 算术运算

## 比较运算

用`all`和`any`来判断。

单纯使用`a[1:3, 1:3] > 20`会返回所有的结果，如果使用`np.all(a[1:3,1:3] > 20)`会判断是否所有选中的都大于20，使用`np.any(a[1:3,1:3] > 20)`会判断是否选中的元素中存在大于20的元素。

使用`allclose`返回两个array是否相等，会逐一比较每个元素，并且允许一定的误差，默认为1e-05。

```
numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)[source]
```

参考：

- [np.allclose(np.array(a), np.array(b))](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)


# 数组修改


## 修改值

创建的多维数组，进行赋值的时候会将指定的行或者元素进行统一赋值。比如如下创建2行3列的ndarray，然后将首行的所有列值赋值为100。

```
paths = np.zeros((2, 3), np.float64)
paths[0] = 100
```


## 修改类型

如果想转换数组的类型，可以通过`float_arr = arr.astype(np.float64)`来完成。


## 修改形状

修改数组的形状也成为“重塑”。

```
b = a.reshape([3, 8]) # 将之前4x6转换为3x8
c = a.reshape([-1, 12]) # 将之前4x6转换为2x12，-1这里表示自动按照列来计算得到的值
d = a.T # 转置
```

*使用`reshape`可以很方便的创建ndarray，比如创建一个3x3的值从0到9的数组，可以使用`np.arange(9).reshape([3, 3])`一下子搞定。*


## 去重

```
np.unique(arr)
```


## 降维

返回将多维数组降为一维的数据。

```
>>> a = np.array([[1,2], [3,4]])
>>> a.flatten()
array([1, 2, 3, 4])
```

参考：

- [numpy.ndarray.flatten](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html)


## 矩阵

使用`np.mat()`来将`ndarray`转换为`matrix`。

```
A = np.mat(a)
```



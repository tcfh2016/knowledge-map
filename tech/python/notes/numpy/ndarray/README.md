# [The N-dimensional array (ndarray)](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)

ndarry是基于相同类型的多维容器。


## 数据打印

### 1.数组属性

- ndarray.ndim 	秩，即轴的数量或维度的数量
- ndarray.shape：数组的维度，对于矩阵，n 行 m 列
- ndarray.size：数组元素的总个数，相当于 .shape 中 n*m 的值


## [numpy.ndarray.flatten](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html)

返回将多维数组降为一维的数据。

```
>>> a = np.array([[1,2], [3,4]])
>>> a.flatten()
array([1, 2, 3, 4])
```

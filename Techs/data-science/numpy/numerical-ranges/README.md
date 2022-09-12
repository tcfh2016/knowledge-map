# [Numerical ranges](https://www.numpy.org/devdocs/reference/routines.array-creation.html#numerical-ranges)

## [numpy.meshgrid(*xi, **kwargs)](https://www.numpy.org/devdocs/reference/generated/numpy.meshgrid.html)

根据坐标值生成N-D坐标矩阵。

- x1, x2,…, xn : array_like
  - 参数为多个1-D的向量，分别代表不同的坐标系。
- X1, X2,…, XN : ndarray
  - 针对不同的向量，返回值为（N1,N2,N3...Nn）的多维数组，其中Ni = len(xi)。

举个例子，比如代码创建了x,y两个长度为20的向量，代表x,y坐标轴上的值，调用meshgrid(x,y)会返回对应的坐标矩阵，即由x,y两个向量在坐标系上对应点的所有坐标，其中的X是以从xi的维度去索引所有的坐标矩阵。

```
x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y)
```

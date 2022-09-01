## Series

`Series`是Pandas中的一种数据对象，这种数据对象是一个可以囊括任何类型的一维数组，我们可以简单地将它类比为表格中的一列数据。不同的是，`Series`相比普通数组多了一些标记类的信息，这些标记类的信息就是索引信息。

怎么理解呢？

比如列表`[1, 7, 2, 3]`就是一个一维数组，我们知道这个列表的内容包含四个数字：1，7，2，3，它们可以通过0，1，2，3四个数字来进行索引。由于没用对应的变量来存放这些信息，所以我们不能操纵这些索引信息。

但是`Series`就可以，使用`[1, 7, 2, 3]`创建的Series除了拥有1，7，2，3这些具体的数值内容（`value`），而且还拥有标记这些内容的标签（`label`），“标签”是相比“数组索引”更为灵活的设计，它能够更好的操作其中的数据。所以我们可以操作1，7，2，3这些具体的值，也可以操作索引这些元素的标签。


## 通过数组创建

因为是一维数组，所以我们可以直接通过list来创建，创建的时候如果不指定标签，那么默认以数字索引来作为标签：

```
import pandas as pd

a = [1, 7, 2, 3]
myvar = pd.Series(a)

print(myvar)
print(type(myvar))

输出为：

0    1
1    7
2    2
3    3
dtype: int64
<class 'pandas.core.series.Series'>
```

创建的时候通过`index`可以自定义更多样化的标签，比如：

```
a = [1, 7, 2, 3]

myvar = pd.Series(a, index = ["w", "x", "y", "z"])
print(myvar)

输出为：
w    1
x    7
y    2
z    3
dtype: int64
```

所以，我们在访问具体的元素的时候除了能够通过数字索引（myvar[2]），还能够通过标签来访问（myvar['x'])。


## 通过字典创建

我们还可以通过key-value的数据类型（比如dict）来创建，这样字典的key自动作为Series的标签，而value作为Series的value。

```
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)

输出为：

day1    420
day2    380
day3    390
dtype: int64
```

如果这个时候再使用index参数，那么就是“选择功能”：仅从字典calories里面选取index里面指定的这些键对应的数据。

```
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

输出为：

day1    420
day2    380
dtype: int64
```

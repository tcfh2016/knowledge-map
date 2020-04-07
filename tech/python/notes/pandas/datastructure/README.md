Pandas的两个主要数据结构为 Series 和 DataFrame，它们为大多数应用提供了一种可靠的、易于
使用的基础。


# Panel

Panel是Pandas中的一种三维数据表类型，但在版本0.25.0之后就废弃了。在print Panel类型的时
候是无法打印出所有数据的，仅能打印出它的维度信息，比如：

```
<class 'pandas.core.panel.Panel'>
Dimensions: 15 (items) x 3 (major_axis) x 2 (minor_axis)
Items axis: ChiName to PrevClosePrice
Major_axis axis: 2020-01-08 00:00:00 to 2020-01-10 00:00:00
Minor_axis axis: 000903 to 000905
```

- Items axis：坐标轴0，每个条目对应一个DataFrame
- Major_axis：坐标轴1，多个DataFrame的index
- Minor_axis：坐标轴2，多个DataFrame的column

在使用的时候可以用任一索引来选择数据，所选择的数据依然是二维表类型（DataFrame）：

- 以Items axis的值为索引：`panel['item']`-对应的DataFrame以Major_axis为index,Minor_axis为column。
- 以Major_axis的值为索引：`panel.major_xs[index]`-对应的DataFrame以Minor_axis为index,item为column。
- 以Minor_axis的值为索引：`panel.minor_xs[index]`-对应的DataFrame以major_axis为index,item为column。

参考：

- [Python Pandas - Panel](https://www.tutorialspoint.com/python_pandas/python_pandas_panel.htm)

# 常用函数

## div()

和NumPy数组一样，DataFrame和Series之间算术运算会以“广播(broadcasting)”的形式进行，且
默认将Series的索引匹配到DataFrame的列，然后沿着行一直向下广播，也就是说以行为单位求取所
有行的运算值。

如果要匹配行且在列上进行广播，需要在调用算术运算函数时指定匹配的坐标轴，即 axis=0。

```
percent_items = percent_items[:].div(percent_items['营业收入(万元)'], axis=0)
```

## mean()

通过`axis`参数来控制平均值操作：

```
drinks.mean(axis=0) # 求取每列的平均值，求值的方向为从上到下
drinks.mean(axis="index")

drinks.mean(axis=1) # 求取每行的平均值，求值的方向为从左至右
drinks.mean(axis="columns")
```

## sort_values()

对某列的series进行排序：

```
movies.title.order # 旧的排序方法，已经弃用。

movies.title.sort_values()
movies['title'].sort_values() # 默认以升序排列
movies['title'].sort_values(ascending=False) # 以降序排列
```

对整个dataframe以某列为标准进行排序：

```
movies.order('title') # 旧的排序方法，已经弃用。

movies.sort_values('title') # 升序排列，不会更改原有dataframe
movies.sort_values('title', ascending=False) # 降序排列，不会更改原有dataframe
movies.sort_values(['content_rating', 'duration']) # 以两列进行排序
```

## reindex

DataFrame 最初的数据与创建时指定的 index顺序密切相关，通过 reindex方法可以进行重新排列。
在使用 reindex()方法时可以指定一些额外选项，比如 fill_value=0 表示对于其中的 NaN的值全
填写为 0。

```
obj = Series([4.2, 2.3, -1.3, 5.2], index=['d', 'b', 'c', 'a'])
obj1 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
```

## map(f)/applymap(f)

map作用于 Series，applymap作用于 DataFrame，表示对每个元素应用函数f。

# NaN (Not a Number)

pandas中缺失的数据项会被填写为 NaN，表示缺失或NA值。对于NA的处理包括如下几类：

- 使用 isnull()，notnull() 来检查某个值是否为 NA。
- 使用 fillna(), replace() 和 interpolate() 来替换 DataFrame 里面的所有 NA。
- 使用 dropna() 将包含有 NA的行和列删除。

## 滤除缺失数据：dropna(criteria)

对于一个 Series, dropna返回一个仅含非空数据和索引值的 Series:

```
from pandas import Series, DataFrame
import pandas as pd
import numpy as np # NaN 在numpy里定义，因此使用NaN需要先import numpy。

s = Series([1, np.NaN, 3.2, np.NaN, 7])
print(s.dropna()) # 删除含有NaN的全部行
print(s.dropna(axis=1)) # 删除含有NaN的全部行
```

然而，对于DataFrame调用 dropna的处理更复杂一些，因为它会默认丢弃所有包含缺失值的行。此
时有两种调整方法：

  - 传入`how = all`，丢弃全为NA的那些行；
  - 传入`thresh=3`来设定丢弃的标准，表示行超过多少个NA时丢弃；
  - 传入参数`axis=1`来指示对于列的操作。

## 填充缺失数据：fillna(new_value)

在大多数情况下，fillna方法是填充缺失数据的主要函数。

  - df.fillna(0)将所有NaN更改为0。
  - df.fillna({1:0.5, 2:-1})将对应列的NaN填充为对应的值，用`axis=1`来指示不同的轴。
  - 传入`inplace=True`在现有对象上进行修改。

# 参考

- [Python | Pandas DataFrame](https://www.geeksforgeeks.org/python-pandas-dataframe/)
- [pandas 修改 DataFrame 列名](https://www.cnblogs.com/hhh5460/p/5816774.html)
- 《利用Python进行数据分析》
- [object conversion](http://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-object-conversion)

# [Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）以及一组与之相关的数
据标签（即索引）组成。

## Series 创建

1. 由一组数据产生简单的Series，未指定索引时默认创建一个0~N-1（N为数据的长度）的整数型索
引。

```
import pandas as pd

obj = pd.Series([4, 7, 0, -3])
```

2. 指定对各个数据点标记的索引。

```
import pandas as pd

obj = pd.Series([4, 7, 0, -3], index=['d', 'b', 'a', 'c'])
```

3. 通过字典创建

```
import pandas as pd

sdata = {'oli': 1000, 'tae': 2000, 'Oed': 500}
obj = pd.Series(sdata)
```

## Series 读取

1. values, index 获取

通过 Series的 values和 index属性来获取值和索引，注意在返回类型上值是以数组类型（array）返回，而索引则由特定的索引对象（Int64Index）。

比如下面是某个series，如果我们仅仅对它的值感兴趣，那么可以用`series.values[a:b]`来进行切片选取，也可以通过`series.values[[a,b]]`来选择指定的两个值。

```
2020-01-15    5530.03
2020-01-16    5527.67
2020-01-17    5510.05
2020-01-20    5587.54
2020-01-21    5523.94
2020-01-22    5575.51
2020-01-23    5377.74
2020-02-03    4910.90
```

2. 值选取

通过索引的方式选取单个或者多个值。

```
obj['a']
obj[['a', 'd']]
```

## Series 修改

## 其他

1. Series 转换为 list

从DataFrame中获取的Series，如何能够转换为list进行处理？

```
# converting to list
salary_list = data["Salary"].tolist()
```

参考：

- [Python | Pandas Series.tolist()](https://www.geeksforgeeks.org/python-pandas-series-tolist/)

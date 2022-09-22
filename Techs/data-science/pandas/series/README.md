## [Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）以及一组与之相关的标签（即索引）组成。这些标签可以使用“数值”，也可以使用“字符串”表示，也可以指定重复的值。

除了“数值索引”和“字符串索引”这种常规索引外，Series对象还有默认的从0开始编号的“位置索引”，使用“位置索引”访问元素的时候需要使用`iloc`属性。


## 属性

1）`index`属性

Series对象的index属性会返回Index对象，它包含不同的种类：

- 创建时没有指定index，那么默认为RangeIndex
- 指定了整数的index，默认为Int64Index
- 指定了字符串的，默认为Index

2）`dtype`属性

代表Series对象中的元素的数据类型。保存多种不同类型时为`object`。

3）`is_unique`属性

判断Series元素值是否存在重复。


## 方法

- s1.append(s2)：对不同的series进行连接。`ignore_index`参数（默认False）用来控制是否为新加入的Series对象重新分配索引标签。
- del s1['a']：删除s1中标签'a'对应的元素。
- s1.drop(index='a', inplace=True)：删除s1中标签'a'对应的元素。
- s1.drop_duplicates()：删除s1中重复元素，通过`keep`参数（默认值first）来确定策略：first是保存最开始的重复值，last是保存最后的重复值，False是删除所有重复值。


## 创建

1. 由一组数据产生简单的Series，未指定索引时默认创建一个0~N-1（N为数据的长度）的整数型索引。

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

*注：创建时可以指定name属性，这个属性在将Series对象与DataFrame对象进行连接操作时会用到。*


## 读取

通过 Series的`values`和`index`属性来获取值和索引，注意在返回类型上值是以数组类型（ndarry）返回，而索引则由特定的索引对象（Index）。

1. 使用`[]`

用方括号就课可以按照“标签”对Series对象进行引用。放开括号支持切片引用，不过这个时候切片索引的重点是包含在引用范围内的，这与列表中进行切片索引是不同的。

```
obj['a']
obj[['a', 'd']]
```

2. 使用`loc`

使用loc来访问元素那么也是通过索引标签来访问，同样可以支持切片访问，类似`[]`此时切片终点是包含在引用范围内的。

3. 使用`iloc`

如果想以“位置索引”来进行值的引用那么就需要使用iloc属性。进行切片引用时是不包含终点的。


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


## 其他

- 查找最大值的索引

如果我想查找某个Series里面最大的元素对应的索引，那么使用`idxmax()`即可。

参考：

- [max](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html)
- [idxmax](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html)


- Series 转换为 list

从DataFrame中获取的Series，如何能够转换为list进行处理？

```
# converting to list
salary_list = data["Salary"].tolist()
```

参考：

- [Python | Pandas Series.tolist()](https://www.geeksforgeeks.org/python-pandas-series-tolist/)

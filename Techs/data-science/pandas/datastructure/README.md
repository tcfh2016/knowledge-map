# [Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

Series是一种类似于一维数组的对象，它由一组同构数据（各种NumPy数据类型）以及一组与之相关的标签（即索引）组成。这些标签可以使用“数值”，也可以使用“字符串”表示，也可以指定重复的值。

除了“数值索引”和“字符串索引”这种“标签索引”外，Series对象还有默认的从0开始编号的“位置索引”，使用“位置索引”访问元素的时候需要使用`iloc`属性。


## 属性

- `index`属性，Series对象的index属性会返回Index对象，它包含不同的种类：创建时没有指定index，那么默认为RangeIndex。指定了类型为Index。
- `dtype`属性，代表Series对象中的元素的数据类型。保存多种不同类型时为`object`。
- `is_unique`属性，判断Series元素值是否存在重复。


## 方法

- s1.append(s2)：对不同的series进行连接。`ignore_index`参数（默认False）用来控制是否为新加入的Series对象重新分配索引标签。
- del s1['a']：删除s1中标签'a'对应的元素。
- s1.drop(index='a', inplace=True)：删除s1中标签'a'对应的元素。
- s1.drop_duplicates()：删除s1中重复元素，通过`keep`参数（默认值first）来确定策略：first是保存最开始的重复值，last是保存最后的重复值，False是删除所有重复值。


## 创建

1. 由一组数据产生简单的Series，未指定索引时默认创建一个0~N-1（N为数据的长度）的整数型索引。
2. 指定对各个数据点标记的索引。
3. 通过字典创建


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


# [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

DataFrame 是一个包含标签的二维表式的数据结构，由data(数据)、rows(行)、columns(列)组成。它的横纵方向都附带了标签，纵向上的标签称为“索引标签”，横向上的标签称为“列标签”。

DataFrame可被看做是由Series组成的字典（共用同一个索引）。

![](dataframe.png)

DataFrame每列的数据类型可以通过`print(df.dtypes)`显示出来。


*注：DataFrame的单一行或者列均是Series类型，只不过index不同：DataFrame行的index为DataFrame的columns名称，DataFrame列的index为DataFrame的index*


## 属性

- df.shape，显示行、列信息。
- df.size，返回的是行列相乘的数值
- df.dtypes，显示行的类型。
- df.index，获取行标签，Index对象，`list(df.index)`可转成列表。
- df.columns，获取列标签，Index对象，`list(df.columns)`可转成列表。
- df.values，获取所有值，类型为`array`。

*使用`len(df)`所打印出来的是df具有的行个数。*


## 方法

- df.head() ：默认显示前面5行的数据
- df.tail() ：默认显示末尾5行的数据
- df.describe() ：显示对应数据对应里面“数据列”的统计信息，包括count, min, max...
- df.describe(include=['object']) ：显示非数据列的统计信息，包括count, uniq, top, freq
- df.sample(n) : 随机显示n行数据，默认显示1行

也可以使用`to_string()`来全部输出整个DataFrame的内容。


## 数据类型

可以通过`df.dtypes`查看各列的类型，通过`df.info()`函数可以查看更详细的内容。

`df.dtypes`的输出：

```
class      object
math        int32
physics     int32
dtype: object
```

`df.info()`的输出：

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   class    2 non-null      object
 1   math     2 non-null      int32 
 2   physics  2 non-null      int32 
dtypes: int32(2), object(1)
memory usage: 160.0+ bytes
None
```

使用`df = df.convert_dtypes()`进行快速数据类型转换。


## 取消科学计数法的格式

比如下面的time，其实暗含了日期和时间，但是由于是float格式默认按照科学计数法显示了，如何将其全部显示出来？

```
           time  current   high    low       volume         money
0  2.020021e+13    1.987  2.022  1.965  338313044.0  6.753016e+08
0  2.020022e+13    2.071  2.071  2.004  689679516.0  1.411302e+09
0  2.020022e+13    2.090  2.090  2.050  704272926.0  1.461049e+09
0  2.020022e+13    2.054  2.087  2.052  572403776.0  1.184645e+09
```

可以通过如下设置来将DataFrame的展示方式替换为浮点数且保留两位小数，也就取消了默认的科学计数法展示格式。

```
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.float_format', "{:.2f}".format)
pd.set_option('precision', 2)
```

参考：

- [How do I expand the output display to see more columns of a pandas DataFrame?](https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe)


## 输出排版

打印DataFrame输出的格式有些时候并不友好，比如：

![](print_not_aligned.png)


## `rank()`

参考：

- [关于pandas的rank()函数的一点认识](https://zhuanlan.zhihu.com/p/87593543)


## 拷贝一个DataFrame

```
df_sub_copy = df[0:1].copy()
```

- [](https://stackoverflow.com/questions/27673231/why-should-i-make-a-copy-of-a-data-frame-in-pandas)


## ValueError: could not convert string to float

`ValueError: could not convert string to float`错误可能因为获取到的dataframe里面有些是空的，所以无法将对应值转换为float。


- [Decimal place issues with floats and decimal.Decimal](https://stackoverflow.com/questions/286061/decimal-place-issues-with-floats-and-decimal-decimal)
- [How to do Decimal to float conversion in Python?](https://stackoverflow.com/questions/32285927/how-to-do-decimal-to-float-conversion-in-python)

## 变更某一列内容的展现形式

比如现在有一列"日期"是按照“年-月-日”的形式展示的，现在需要让其展现为“年-月”的形式展示，该如何操作？

```
df['month_year'] = df['date_column'].dt.to_period('M')
```

参考：

- [Extracting just Month and Year from Pandas Datetime column](https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-from-pandas-datetime-column)
- [Series.dt ](http://pandas.pydata.org/pandas-docs/stable/reference/series.html#api-series-dt)


## 转换为`dict`

使用`df.to_dict()`可以将一个DataFrame转换为字典的类型，假设之前为15行3列的DataFrame：

- 默认参数`orient='dict'`，转换为以列为单位的字典：包含3个字典的字典，每个字典包含有15个key-pair键值对。
- 指定`orient="records"`，转换为以行为单位的字典列表：包含15个字典的列表，每个字典有3个key-pair键值对。

参考：

- [pandas.DataFrame.to_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)
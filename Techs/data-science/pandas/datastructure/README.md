## [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

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
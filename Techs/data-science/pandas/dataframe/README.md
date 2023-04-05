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

*使用`len(df)`所打印出来的是df具有的行个数。*


## 方法

- DataFrame.head() ：默认显示前面5行的数据。
- DataFrame.describe() ：显示对应数据对应里面“数据列”的统计信息，包括count, min, max...
- DataFrame.describe(include=['object']) ：显示非数据列的统计信息，包括count, uniq, top, freq


## 列的类型

pandas会根据输入的数据来确定每个列的数据类型，比如一列的数据全是int，那么该列的类型就是int，哪怕其中的一个为float，那么该列为float。

将特定列进行类型转换：

```
# convert column "a" to int64 dtype and "b" to complex type
df = df.astype({"a": int, "b": complex})
```


想将整个 DataFrame的值转换为float类型进行计算，尝试`pd.to_numeric(m)`发现只能够转换单维的数据。如果要转换所有列，那么需要使用循环，然而这种方式会返回新的对象，不是在原对象基础上进行转换，使用起来不方便。

*注：调用`to_numeric()`时根据原有数据决定转换为`int64`还是`float64`。*

```
for col in float_df:
    print(pd.to_numeric(float_df[col]))
```

通过`print(df.dtypes)`打印DataFrame各列的类型。


参考：

- [](https://stackoverflow.com/questions/15891038/change-column-type-in-pandas)

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

## 什么是`Panel`类型

Panel是Pandas中的一种三维数据表类型，但在版本0.25.0之后就废弃了。在print Panel类型的时候是无法打印出所有数据的，仅能打印出它的维度信息，比如：

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

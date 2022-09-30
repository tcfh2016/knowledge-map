
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

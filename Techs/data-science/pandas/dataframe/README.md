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


## 获取行列名


## DataFrame 类型转换

想将整个 DataFrame的值转换为float类型进行计算，尝试`pd.to_numeric(m)`发现只能够转换单维的数据。如果要转换所有列，那么需要使用循环，然而这种方式会返回新的对象，不是在原对象基础上进行转换，使用起来不方便。

*注：调用`to_numeric()`时根据原有数据决定转换为`int64`还是`float64`。*

```
for col in float_df:    
    print(pd.to_numeric(float_df[col]))
```

通过`print(df.dtypes)`打印DataFrame各列的类型。


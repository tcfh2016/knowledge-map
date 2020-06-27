## [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

DataFrame 是一个二维表式的数据结构，由data(数据)、rows(行)、columns(列)组成，数据基于
行列进行存储，因此它既有行索引也有列索引，可被看做是由Series组成的字典（共用同一个索引）。

![](dataframe.png)

DataFrame每列的数据类型可以通过`print(df.dtypes)`显示出来。

- object: 字符串类型。


## 索引

- [层次化索引](./hierarchical_index/README.md)

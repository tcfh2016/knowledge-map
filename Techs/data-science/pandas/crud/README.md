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
- s1.add(s2, fill)，是将两者的值相加。


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

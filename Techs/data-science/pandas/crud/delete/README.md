# 删除

## 删除行列

删除行或者列的时候可以调用`drop()`方法，删除时的`axis`用来指定坐标轴。默认为`axis=0`，删除行标签对应的行（行标签对应的所有列有效），如果设置为`axis=1`则删除列标签对应的列（列标签对应的所有行有效）。

```
df.drop([0,1], axis=0, inplace=True) # 删除index为0，1的行。
df.drop('column name', axis=1) # 指定axis=1说明删除列。
df.drop(['city', 'state'], axis=1) # 删除'city'和'state'两列。
```

删除多个行或者列时只需要将所有行/列以列表的形式传入，比如`df.drop(df[<some boolean condition>].index)`。更高效的方式是`df = df[df.score > 50]`。

另外还有一种方法，是使用`del`。删除列时必须通过索引的方式指定，不能通过属性的方式来指定。

```
del df['newdata']
del df.newdata # 会提示错误。n 
```

按照制定条件删除，比如删除值小于0所在的行？使用:

```
df = df[(df > 0).all(axis=1)]
```

参考：

- [How to delete rows from a pandas DataFrame based on a conditional expression](https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression)


## pandas.read_csv 删除行或列

从DataFrame删除行时需要使用drop函数，删除对应行需要指定index并且axis设定为“0”，删除列时需要指定列名且axis设定为“1”。

```
data = data.drop([0,1,2], axis=0)

data = data.drop("Area", axis=1)
data = data.drop(columns="area") # 这种方式不需要指定 axis参数。
```

如果需要删除满足某些条件的行，分两步走：

- Step 1 过滤出对应的行: df_age_negative = df[ df['Age'] < 0 ]
- Step 2 调用drop进行删除: df = df.drop(df_age_negative.index, axis=0)

参考：

[How to drop a list of rows from Pandas dataframe?](https://stackoverflow.com/questions/14661701/how-to-drop-a-list-of-rows-from-pandas-dataframe)
[The Pandas DataFrame – loading, editing, and viewing data in Python](https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/)


# 缺失值

## NaN (Not a Number) 处理

pandas中缺失的数据项会被填写为`NaN`，它仅仅是一个占位符，用来表示该单元的值是缺失的。对于缺失值的处理包括如下几类：

- 使用`obj.isnull()`，`pd.isnull(cell)`, `obj.notnull()`, `pd.notnull(cell)` 来检查NA。
- 使用 fillna(), replace() 和 interpolate() 来替换 DataFrame 里面的所有 NA。
- 使用 dropna() 将包含有 NA的行和列删除。

对于Series/DataFrame对象来说，`obj.isnull()`返回一个boolean类型的Series对象，如果我们仅想检查该Series是否包含有缺失值直接使用`obj.isnull().values.any()`即可。使用`obj.isnull().sum()`可以针对按照Series维度进行缺失数据的统计，而后面再加个.sum()即`obj.isnull().sum().sum()`可以统计出整个DataFrame的缺失值个数。

如果要测试单个值，那么可以使用`pd.isnull()`或者`pd.notnull()`。

*注意：NaN参与的所有计算都是NaN。*
*使用`mys.isnull().all()`来判断一列是否全是NaN。*

参考：

- [How to Check If Any Value is NaN in a Pandas DataFrame](https://chartio.com/resources/tutorials/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe/)


## 为什么一定要提前处理好`NaN`

有时候通过`df = df[(df['code'].str.startswith('*ST')) & (df['code'].str.find('500') != -1])`的方式不一定找得到匹配的行，可能原因：

原始数据里面有无效值`NaN`，然后使用`df['code'].str.find('500') != -1]`也会返回`True`因为对于`NaN`来说也是成立的：调用find()返回NaN，NaN != -1成立。


## NaN 的显示

使用`pd.read_csv()`读取csv时，有时候尽管某列是`object`类型，也就是有值的单元格类型为`str`，但是空的单元格类型却是`float`，在表格里面显示为`NaN`，打印出来显示为`nan`。

如果用这些`NaN`值去匹配，比如`df['c'].str.find('abc') != -1`都会为`True`。如果要使用字符匹配，必须要先填充这些无效值。


## `np.nan`/`np.NaN`与`None`的区别

首先，`np.nan`和`np.NaN`（甚至`np.NAN`，都是别名）实际上是同一个东西，那它们到底是一个什么值？打印出它的类型是`float`，但是np.nan和np.nan并不相等，所以你无法使用`==`来进行比较，`np.nan`本身使用`==`测试也是`False`。

- 使用`np.nan is np.NaN`返回`True`。
- 使用`np.isnan(np.nan)`返回`True`。

从类型上，`np.nan`的类型是`float`，`None`的类型是`object`，两者从数据类型上是不同的，而从Python的执行效率上讲，object==bad, float==good。


不过在[What is the difference between NaN and None?](https://stackoverflow.com/questions/17534106/what-is-the-difference-between-nan-and-none)里提到`np.isnan(p)`对传入的参数有要求，如果是string类型那么会crash，使用`pd.isnull()`则要安全得多。


参考：

- [Why does assert np.nan == np.nan cause an error?](https://stackoverflow.com/questions/44367557/why-does-assert-np-nan-np-nan-cause-an-error)。
- [What is the difference between NaN and None?](https://stackoverflow.com/questions/17534106/what-is-the-difference-between-nan-and-none)
- [Difference between np.nan and np.NaN](https://stackoverflow.com/questions/53436339/difference-between-np-nan-and-np-nan)


## 滤除缺失数据：dropna(criteria)

对于一个 Series, dropna返回一个仅含非空数据和索引值的 Series:

```
from pandas import Series, DataFrame

s = Series([1, np.NaN, 3.2, np.NaN, 7])
print(s.dropna()) # 删除含有NaN的全部行，注意Series是单列多行的数据，而非单行
print(s.dropna(axis=1)) # 删除含有NaN的全部列
```

然而，对于DataFrame调用 dropna的处理更复杂一些，因为它会默认丢弃所有包含缺失值的行。此时有两种调整方法：

  - 传入`how = all`，丢弃全为NA的那些行；
  - 传入`thresh=3`来设定丢弃的标准，个数是有效值的个数，有效值不达标的丢弃；
  - 传入参数`axis=1`来指示对于列的操作。


## 仅仅删除某列值为空的数据

```
df = df[df.line_race != 0]
df = df[df.line_race.notnull()]
```

参考：

- [Deleting DataFrame row in Pandas based on column value](https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value)


## 填充缺失数据：fillna(new_value)

在大多数情况下，fillna方法是填充缺失数据的主要函数。

  - df.fillna(0)将所有NaN更改为0。
  - df.fillna({1:0.5, 2:-1})将对应列的NaN填充为对应的值，用`axis=1`来指示不同的轴。
  - 传入`inplace=True`在现有对象上进行修改。

碰到一个问题：在将某一列转换为`int`类型的时候，有些是`NaN`便会失败。


## 参考

- [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)


# 重复数据

## 查看重复行

通过`df.duplicated(keep='first')`来对重复数据进行检测，返回的结果是一个bool类型的Series对象，其中的keep参数是用来判定第一次重复数据的标记，可以接受`first`, `last`和`False`选项，False会将所有的重复数据返回True。

当然，还可以真对特定列进行重复数据的检查，比如`df.duplicated(subset='a', keep='first')`就是只针对'a'列进行。

得到了bool类型的Series后，我们可以通过`df[df.duplicated](keep=False)]`直接引用重复的行。


## 处理重复行

函数`drop_duplicates()`用来移除重复行，原型如下：

```
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
```

支持三个参数：subset某列或者列名的列表，表示参考那些列来对比重复；keep表示处理重复记录时保存哪一条；inplace表示将修改应用到原来的dataframe里。

参考：

- [pandas.DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)
- [Python | Pandas dataframe.drop_duplicates()](https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/)

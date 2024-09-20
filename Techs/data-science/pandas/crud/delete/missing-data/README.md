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
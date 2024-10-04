# 需要特别留意

## 为什么一定要提前处理好`NaN`

有时候通过`df = df[(df['code'].str.startswith('*ST')) & (df['code'].str.find('500') != -1])`的方式不一定找得到匹配的行，可能原因：

原始数据里面有无效值`NaN`，然后使用`df['code'].str.find('500') != -1]`也会返回`True`因为对于`NaN`来说也是成立的：调用find()返回NaN，NaN != -1成立。


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

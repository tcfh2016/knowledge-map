
## 增加行列

在某个DataFrame里面添加一列必须使用`[]`操作符，`此时应保证Series和DataFrame具有相同的index`

```
df['numbers'] = series
```


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


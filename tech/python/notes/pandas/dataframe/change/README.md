## 修改DataFrame

### 行、列名的修改

1.修改行名

直接赋值，如下将DataFrame的index修改为其中的某一列：

```
min_max_df.index = min_max_df['日期'] # 之前的'日期'列依然存在
min_max_df = min_max_df.set_index('日期', drop=True) #

# 这种方式复写之前的index后，索引的名字也不见了。
# 使用 df.index.name = xx 来写入。
df.index = [1, 2, 3, 4]
```


*注1：DataFrame的set_index函数会将一个或多个列转换为行索引，并创建新的DataFrame。*
*注2：Index 对象是不可修改的。因此df.index[1] = 'c'会提示错误。*

参考：

- [Remove index name in pandas](https://stackoverflow.com/questions/29765548/remove-index-name-in-pandas)

2.修改列名

两种方式：直接赋值和调用 rename方法：

```
df.columns = ['price'] # 用等长的列表来覆盖之前的列名
df.rename(columns=lambda x:x.replace('$',''), inplace=True)
df.rename(columns={'a':'b'}, inplace=True) # 将'a'重命名为'b'，可以支持多列的重命名。
```

另外在read_csv()的时候可以修改读取数据的列名：

```
ufo = pd.read_csv(name_file, names=ufo_cols, header=0) # 不指定header，直接使用自
定义ufo_cols作为列名。
```

### 增/删行、列

1.增加行

在某个DataFrame里面添加一列必须使用`[]`操作符，`此时应保证Series和DataFrame具有相同的index`

```
df['numbers'] = series
```

2.删除行

调用`drop()`:

```
df.frop([0,1], axis=0, inplace=True) # 删除index为0，1的行。
```

3.删除列

两种方法：调用`drop()`和使用`del`。

`drop()`函数可以用来删除行和列。

```
df.drop('column name', axis=1) # 指定axis=1说明删除列。
df.drop(['city', 'state'], axis=1) # 删除'city'和'state'两列。
```

删除列时必须通过索引的方式指定，不能通过属性的方式来指定。

```
del df['newdata']
del df.newdata # 会提示错误。
```

4.处理重复行

函数`drop_duplicates()`用来移除重复行，原型如下：

```
DataFrame.drop_duplicates(subset=None, keep=’first’, inplace=False)
```

支持三个参数：subset某列或者列名的列表，表示参考那些列来对比重复；keep表示处理重复记录时保存哪一条；inplace表示将修改应用到原来的dataframe里。

参考：

- [pandas.DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)
- [Python | Pandas dataframe.drop_duplicates()](https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/)


### 修改行、列

1.修改整列

直接通过赋值的方式修改（添加）：

```
df['numbers'] = 1.0
df.numbers = 1.0
```

将列表或数组赋值给某列时，其长度必须跟DataFrame的长度匹配：

```
val = Series([-1, -2, -3, -4], index=['b', 'a', 'c', 'd'])
df['newdata'] = val
df.newdata = val
```

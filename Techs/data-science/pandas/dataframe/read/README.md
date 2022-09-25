## 获取列：方括号`[]`

通过方括号`[]`，可以将 DataFrame的列获取为一个Series。多列的选取需要将多个列的名称作为列表放在方括号中。

```
df['Age'] # 选取单列
df[['Age','Name']] # 选取多列
df.Age  # 这种方式很简洁，但是如果某个行名由多个单词组成，比如‘start time’就无法工作了。
```

*那么如何将某列转换为`list`类型呢？可以通过`df['Age'].values.tolist()`或者直接`list(df['Age'])`也可以。*

需要注意DataFrame的获取是以列优先的，比如dataframe[x]是获取列名为x的对应的Series，这种理解方式与C/C++二维数组是不同的。


## 获取列的另一种方式：`loc()`和`iloc`

通过`loc()`和`iloc`属性我们可以很方便的获取列、行、以及行列对应的值，语法为`loc[行标签, 列标签]`。它们之间的不同之处在于，前者需要使用行列标签，后者需要使用位置索引。

1）获取列

```
df.loc['a', :] # 获取'a'行
df.loc[['a', 'b'], :] # 获取'a', 'b'两行

df.loc['a'] # 获取'a'行
df.loc[['a', 'b']] # 获取'a', 'b'两行

df.iloc[3] # 选择一行
df.iloc [[3, 5, 7]] # 选择三行
```

2）获取行

```
df.loc[:, 'a']  # 获取'a'列
df.loc[:, ['a', 'b']] # 获取'a', 'b'两列


```

3）获取行列

```
# 行索引为数字，列索引为字符串
df.iloc[0]['col']
df['col'].iloc[0] #更快

# 行、列索引均为字符串
df.loc['row_name']['col_name']
df.loc['row_name', 'col_name']

data.iloc [[3, 4], [1, 2]] # 选择两行两列
```

怎么判断一个单元格是否存在呢？直接通过字符串索引去找：`row in df.index.values and col in df.columns.values`。


参考：

- [Indexing and Selecting Data with Pandas](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)
- [](https://stackoverflow.com/questions/28754603/indexing-pandas-data-frames-integer-rows-named-columns)



## 使用切片

切片支持行名称和行序号来确定范围（*DataFrame仅能用行进行切片*）：

```
print(df['a':'c'])        # 索引'a', 'b', 'c'三行。
print(df[0:1])            # 索引'a'一行数据。
```


## 使用布尔索引

根据列的条件来进行选择，这种方式是pandas所独有的方式。

```
df[df.A > 0]    # 以某列的数据做为标准选择数据
df[df['A'] > 0] # 以某列的数据做为标准选择数据
df[df > 0]      # 选择 df中大于0的数，其余置为 NaN
```

简单地说，pandas支持df[SeriesOfBollean]来选取行，而实际上SeriesOfBollean的创建可以通过简单的df.column > contion来完成。

```
conditions = []
for f in df.floats:
    if f > 3.0:
        conditions.append(True)
    else:
        conditions.append(False)
print(df[conditions])
match_condition = pd.Series(conditions, index=df.index)
print(df[match_condition])
```

如上的代码与下面这段等价：

```
print("按条件选择行例3：")
condition = df.floats > 3.0  # 创建一个bollean 的Series。
print(df[condition])
```

对于`datetime.date`类型如何通过布尔索引来进行呢？创建`compare_date = datetime.date(2012, 1, 1)`在进行比较，否则提示：

```
not supported between instances of 'datetime.date' and 'str'
```

在pandas里面如果要使用字符串来过滤特定的行，那么必须要使用`.str`属性才可以：

```
df = df[df['code'].str.startswith('*ST')]
df = df[df['code'].str.find('500') != -1]
```

如何附加多个条件？使用逻辑表达式即可。如`df = df[df['code'].str.startswith('*ST') & df['code'].str.find('500') != -1]`。


如果我们想选取所有列均匹配某种条件的所有行的数据，参考[](https://stackoverflow.com/questions/32731498/how-to-select-cells-greater-than-a-value-in-a-multi-index-pandas-dataframe)可以找到方案，即使用`.all(axis=1)`：

```
In [9]: df
Out[9]:
   A  B  C
0  1  2  3
1  3  4  5
2  3  1  4
3  1  2  1

In [11]: df[(df <= 2).all(axis=1)]
Out[11]:
   A  B  C
3  1  2  1
```

*注：在选择之后Index是不会更新的，如果需要迭代读取每个数值，那么就需要重新reset_index来重新索引。*

```
sales_data.reset_index(drop = True)
```

参考：

- [How do I filter rows of a pandas DataFrame by column value?](https://www.youtube.com/watch?v=2AFGPdNn4FM)
- [How to filter Pandas Dataframe rows which contains any string from a list?](https://stackoverflow.com/questions/55941100/how-to-filter-pandas-dataframe-rows-which-contains-any-string-from-a-list)


Q1: 怎样获取数值索引对应行的名字？

答：只需要将对应索引的行都选出来，选出来的这部分实际上是一个新的dataframe，所以就可以通过它的index得到其行名称，如`list(df.iloc[[0, 1, 3]].index)`表示先选择出第0，1，3行然后将其index转换为list。

参考：

- [How do I get the name of the rows from the index of a data frame?](https://stackoverflow.com/questions/26640145/how-do-i-get-the-name-of-the-rows-from-the-index-of-a-data-frame)

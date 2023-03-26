## 选取列

列的选取是DataFrame最基本的操作，使用方括号`[]`，将 DataFrame的列获取为一个Series。多列的选取需要将多个列的名称作为列表放在方括号中。

```
df['col1_label'] # 选取单列
df[['col1_label', 'col2_label']] # 选取多列
```

DataFrame的获取是以列优先的，`df[x]`是获取列名为x的Series，这种理解方式与C/C++二维数组是不同的。

*那么如何将某列转换为`list`类型呢？可以通过`df['Age'].values.tolist()`或者直接`list(df['Age'])`也可以。*


## 选取行

通过`loc()`和`iloc`属性用于获取行或行列对应的值。它们之间的不同之处在于，前者需要使用行列标签，后者需要使用位置索引。

```
df.loc['a'] # 获取'a'行
df.loc[['a', 'b']] # 获取'a', 'b'两行

df.iloc[3] # 选择一行
df.iloc[[3, 5, 7]] # 选择三行
```


## 使用切片

使用切片功能，切片支持行名称和行序号来确定范围（*DataFrame仅能用行进行切片*）：

```
print(df['a':'c'])        # 索引'a', 'b', 'c'三行。
print(df[0:1])            # 索引'a'一行数据。
```


## 选取数据单元

因为索引有标签索引和位置索引两种形式，所以在选取数据单元的时候存在可能的混用情况：

- 行、列索引均为字符串，可以用`df.loc['row_label']['col_label']`或者`df.loc['row_label', 'col_label']`。
- 行、列索引均为位置索引，可以用`data.iloc [[3, 4], [1, 2]]`选择两行两列。
- 行索引为数字，列索引为字符串，可以用`df.iloc[0]['col']`或者`df['col'].iloc[0]`。


使用位置索引的时候比较少，因为如果要使用位置索引那么你还得一个一个去数，这在数据量大的时候是很难办的。

参考：

- [Indexing and Selecting Data with Pandas](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)
- [Indexing Pandas data frames: integer rows, named columns](https://stackoverflow.com/questions/28754603/indexing-pandas-data-frames-integer-rows-named-columns)


## 布尔索引

根据列的条件来进行选择，这种方式是pandas所独有的方式。

```
df[df.A > 0]    # 以某列的数据做为标准选择数据
df[df['A'] > 0] # 以某列的数据做为标准选择数据
df[df > 0]      # 选择 df中大于0的数，其余置为 NaN
```

简单地说，pandas支持df[SeriesOfBollean]来选取行，而实际上SeriesOfBollean的创建可以通过简单的`df.column > contion`来完成。

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

pandas里面如果要使用字符串来过滤特定的行，那么必须要使用`.str`属性才可以：

```
df = df[df['code'].str.startswith('*ST')]
df = df[df['code'].str.find('500') != -1]
```

如何附加多个条件？使用逻辑表达式即可。如`df = df[(df['code'].str.startswith('*ST')) & (df['code'].str.find('500') != -1])`。


如果我们想选取所有列均匹配某种条件的所有行的数据，使用`.all(axis=1)`：

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
- [How to select cells greater than a value in a multi-index Pandas dataframe?](https://stackoverflow.com/questions/32731498/how-to-select-cells-greater-than-a-value-in-a-multi-index-pandas-dataframe)



## 遍历行

```
for index, row in df.iterrows():
    print(row['c1'], row['c2'])
```

参考：

- [How to iterate over rows in a DataFrame in Pandas](https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)


## 不常用/不推荐

df.Age  # 这种方式很简洁，但是如果某个行名由多个单词组成，比如‘start time’就无法工作了。
df.loc[:, 'a']  # 获取'a'列
df.loc[:, ['a', 'b']] # 获取'a', 'b'两列



## Cannot perform 'rand_' with a dtyped...

想根据两列的查询数据来查询满足条件的行时提示“`Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]`”

```
df = df[df['市盈率(TTM)'] < 5.0 & df['市净率'] < 0.5]
```

解决方案，在不同条件上加上括号。比如上面的修改为：

```
df = df[(df['市盈率(TTM)'] < 5.0) & (df['市净率'] < 0.5)]
```

参考：

- [TypeError: Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]](https://stackoverflow.com/questions/60654781/typeerror-cannot-perform-rand-with-a-dtyped-float64-array-and-scalar-of-ty)
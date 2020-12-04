## 访问DataFrame

需要注意DataFrame的获取是以列优先的，比如dataframe[x]是获取列名为x的对应的Series，这种
理解方式与C/C++二维数组是不同的。

### 获取行列名

通过`df.columns`选中所有列名。通过`df.index`选中所有行名。


### 获取列

通过类似字典标记或属性的方式，可以将 DataFrame的列获取为一个 Series。多列的选取需要指
定多个列的名称，切片默认用来选取多行，因此想要在多列选取的时候使用切片必须采用`混合索引/
同时选择行和列`的方式，即`obj.ix[val1,val2]`，在val2里使用切片。

```
df.Age  # 这种方式很简洁，但是如果某个行名由多个单词组成，比如‘start time’就无法工作了。
df['Age'] # 选取单列
df[['Age','Name']] # 注意多列
```

一次性指定多个列的名称可以同时选中两列，比如如上例子里面`df['Name', 'Age']`。

### 获取行

行的选取有三种方式：`loc`方法、切片和布尔索引（Boolean indexing）。

**1.使用`loc`方法**

使用`loc`方法通常用来进行单行索引，在选择多行时语法上与列有些类似。

```
df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

print(df.loc['b'])        # 通过索引访问元素，之前是df.ix['b']，已不推荐使用旧的方法。
print(df.loc[['a', 'b']]) # 索引'a', 'b'两行。
```

**2.使用切片**

切片支持行名称和行序号来确定范围（*DataFrame仅能用行进行切片*）：

```
print(df['a':'c'])        # 索引'a', 'b', 'c'三行。
print(df[0:1])            # 索引'a'一行数据。
```

**3.使用布尔索引**

根据列的条件来进行选择，这种方式是pandas所独有的方式。

```
df[df.A > 0]    # 以某列的数据做为标准选择数据
df[df['A'] > 0] # 以某列的数据做为标准选择数据
df[df > 0]      # 选择 df中大于0的数，其余置为 NaN
```

简单地说，pandas支持df[SeriesOfBollean]来选取行，而实际上SeriesOfBollean的创建可以通
过简单的df.column > contion来完成。

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

对于`datetime.date`类型如何通过布尔索引来进行呢？创建`compare_date = datetime.date(2012, 1, 1)`
在进行比较，否则提示：

```
not supported between instances of 'datetime.date' and 'str'
```

在pandas里面如果要使用字符串来过滤特定的行，那么必须要使用`.str`属性才可以：

```
df = df[df['code'].str.startswith('*ST')]
```

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

参考：

- [How do I filter rows of a pandas DataFrame by column value?](https://www.youtube.com/watch?v=2AFGPdNn4FM)
- [How to filter Pandas Dataframe rows which contains any string from a list?](https://stackoverflow.com/questions/55941100/how-to-filter-pandas-dataframe-rows-which-contains-any-string-from-a-list)


### 获取多行多列

```
df.loc[:, ['A', 'B']]
```

### 获取某行某列的值

*注：DataFrame的单一行或者列均是Series类型，只不过index不同：DataFrame行的index为DataFrame
的columns名称，DataFrame列的index为DataFrame的index*

- Dataframe.[ ] ; This function also known as indexing operator
- Dataframe.loc[ ] : This function is used for labels.
- Dataframe.iloc[ ] : This function is used for positions or integer based
- Dataframe.ix[] : This function is used for both label and integer based

获取某行某列的值仅仅是获取多行多列的值的简化形式。如上最后一种方法已经过时。

```
data["Age"] # 选择列名为Age的一列
data[["Age", "College", "Salary"]] # 选择列名为Age, College, Salary的三列

data.loc["R.J. Hunter"] # 选择行名为R.J. Hunter的一行
data.loc[["Avery Bradley", "R.J. Hunter"]] # 选择行名为Avery Bradley, R.J. Hunter的三行
data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]] # 选择两行三列

data.iloc[3] # 选择一行
data.iloc [[3, 5, 7]] # 选择三行
data.iloc [[3, 4], [1, 2]] # 选择两行两列
```

参考：

- [Indexing and Selecting Data with Pandas](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)


## DataFrame 查询

1.判断DataFrame是否为空

```
if df.empty:
    print('DataFrame is empty!')

len(df.index) == 0    
```

参考：

- [How to check whether a pandas DataFrame is empty?](https://stackoverflow.com/questions/19828822/how-to-check-whether-a-pandas-dataframe-is-empty)

2.根据某列的值查询对应的index

因为index是行索引，引起可以借助条件选择的功能选择特定的行，然后再获取结果的index属性：

```
stocks_df[stocks_df['display_name'] == '洋河股份'].index
结果为：Index(['002304.XSHE'], dtype='object')

stocks_df[stocks_df['display_name'] == '洋河股份'].index.item()
结果为：002304.XSHE
```

参考：

- [Python Pandas: Get index of rows which column matches certain value](https://stackoverflow.com/questions/21800169/python-pandas-get-index-of-rows-which-column-matches-certain-value)
- [Get index of a row of a pandas dataframe as an integer](https://stackoverflow.com/questions/41217310/get-index-of-a-row-of-a-pandas-dataframe-as-an-integer/41217335)

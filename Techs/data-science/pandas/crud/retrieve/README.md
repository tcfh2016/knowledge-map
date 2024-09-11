## 判断DataFrame是否为空

```
if df.empty:
    print('DataFrame is empty!')

len(df.index) == 0    
```

参考：

- [How to check whether a pandas DataFrame is empty?](https://stackoverflow.com/questions/19828822/how-to-check-whether-a-pandas-dataframe-is-empty)


## 判断一个单元格是否存在

直接通过字符串索引去找：`row in df.index.values and col in df.columns.values`。

## 判断值在某列中是否存在

可以使用`if 'C' in df['class'].values`来判断。


## 判断某列是否包含特定字符串

在pandas里面如果要使用字符串来过滤特定的行，那么必须要使用`.str`属性才可以：

```
df = df[df['code'].str.startswith('*ST')]
df = df[df['code'].str.find('500') != -1]
```


## 获取数值索引对应行的名字

答：只需要将对应索引的行都选出来，选出来的这部分实际上是一个新的dataframe，所以就可以通过它的index得到其行名称，如`list(df.iloc[[0, 1, 3]].index)`表示先选择出第0，1，3行然后将其index转换为list。

参考：

- [How do I get the name of the rows from the index of a data frame?](https://stackoverflow.com/questions/26640145/how-do-i-get-the-name-of-the-rows-from-the-index-of-a-data-frame)


## 最大值查询

print(df["score"].max())
print(df["score"].idxmax())


## 根据某列的值查询对应的index

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


## 按照某列的数据进行拆分

需求：按照某列的值进行区分。并且分拆到不同的DataFrame里面？


## 怎么知道某列有哪些值？

可以使用`unique()`函数，如`dataframe["column"].unique()`或者`pd.unique(1d array-like)`就可以得到一个一维列表。


然后，我们就可以通过条件选择来过滤，从而将一个DataFrame拆分为多个DataFrame。

参考：

- [What is the unique function in pandas?](https://www.educative.io/answers/what-is-the-unique-function-in-pandas)


## 第二个问题：怎样按照值的范围进行拆分？

参考：

- [Pandas Groupby Range of Values](https://stackoverflow.com/questions/21441259/pandas-groupby-range-of-values)


## 遍历

1.简单遍历

对于Series, Dataframe的遍历操作如下：

```
for c in ufo.city:
  print(c)

for index, row in ufo.interrows():
  print(index, row.City, row.State) # 打印City, State

```

## 通过多列的值来进行行选取操作

比如如下数据，我要将“所有列内容都小于某个值”的那些行删除掉，改如何操作？

```
                               002352     600233
报告日期
货币资金(万元)               1613112.0   406144.0
结算备付金(万元)                   0.0        0.0
拆出资金(万元)                     0.0        0.0
交易性金融资产(万元)               1444.0       79.0
衍生金融资产(万元)                  0.0        0.0
```

学习了DataSchool的一个视频，知道通过条件选择的原理来自于构建一个bolean的Series，因此可以对这两列的内容进行求与操作来构建这样的series：

```
filter_condition = [True] * len(self.balance_df[0]['2018-12-31'])
for i in range(len(self.args.stock)):
    s = self.args.stock[i]
    self.multi_stocks_asset_df[s] = self.balance_df[i]['2018-12-31']
    filter_condition &= self.multi_stocks_asset_df[s] > 0

df_for_plot = self.multi_stocks_asset_df[filter_condition]
```

学习了另外一个视频之后，才知道通过多列来进行选择需要使用`&`或者`|`将条件进行逻辑计算，即便如此，如要根据多列（事前未知）来进行选取依然需要使用如上代码实例里的方式。

```
df_for_plot = self.multi_stocks_asset_df[condition1 & condition2]
```

而对于单列多条件的选取，可以使用简便的方式:

```
movies[(movies.genre=='Crime') | (movies.genre=='Drama') | (movies.genre=='Action')]
movies[movies.genre.isin(['Crime', 'Drama', 'Action'])]
```

查看[How to iterate over rows in a DataFrame in Pandas](https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas)知道看起来简单的方案，但是效率似乎比较低。

```
df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})

for index, row in df.iterrows():
    print(row['c1'], row['c2'])
```

好在[Different ways to iterate over rows in Pandas Dataframe](https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/)这里有其他方案：

```
for ind in df.index:
     print(df['Name'][ind], df['Stream'][ind])

for i in range(len(df)) :
  print(df.loc[i, "Name"], df.loc[i, "Age"])
```


参考：

- [How do I filter rows of a pandas DataFrame by column value?](https://www.youtube.com/watch?v=2AFGPdNn4FM)
- [How do I apply multiple filter criteria to a pandas DataFrame?](https://www.youtube.com/watch?v=YPItfQ87qjM)

## 选取列

列的选取是DataFrame最基本的操作，使用方括号`[]`，将 DataFrame的列获取为一个Series。多列的选取需要将多个列的名称作为列表放在方括号中。

```
df['col1_label'] # 选取单列
df[['col1_label', 'col2_label']] # 选取多列
df.loc[:, 'col1_label':'col2_label'] # 选取多列
```

DataFrame的获取是以列优先的，`df[x]`是获取列名为x的Series，这种理解方式与C/C++二维数组是不同的。

*那么如何将某列转换为`list`类型呢？可以通过`df['Age'].values.tolist()`或者直接`list(df['Age'])`也可以。*

## 不选择某些列


不选择单列：

```
df.loc[:, df.columns!='rebounds']
```

不选择多列：

```
df.loc[:, ~df.columns.isin(['rebounds', 'assists'])]
```

参考：

- [](https://www.statology.org/pandas-exclude-column/)

## 选择特定的行


查了资料，没有找到直接的方法，想了想有两种：

- 使用转置T进行选择

```
selected_columns = df.loc[:, df.columns.str.contains('NewYork')]
```

- 使用列删除


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

- 行、列索引均为字符串，可以用`df.loc['row_label', 'col_label']`或者`df.loc['row_label']['col_label']`。或者`df.at['row_label', 'col_label']`
- 行索引或列索引为位置索引时，可以用`df.iloc[0]['col']`/`df.iloc[0][1]`或者`df['col'].iloc[0]`。


使用位置索引的时候比较少，因为如果要使用位置索引那么你还得一个一个去数，这在数据量大的时候是很难办的。

*注1：有些版本，比如pandas 1.3.1 里面，使用df.iloc[x][label]来赋值就不生效。*
*注2：`at`方法赋值的时候会进行隐式类型转换，比如原来的列是`int`，赋值的是`float`，会执行`float -> int`转换。*
*注3：为了方便起见，在使用`loc`的时候采用`[]`的写作方法，使用`iloc`的时候采用`[][]`数组形式的方法。*

参考：

- [Indexing and Selecting Data with Pandas](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)
- [Indexing Pandas data frames: integer rows, named columns](https://stackoverflow.com/questions/28754603/indexing-pandas-data-frames-integer-rows-named-columns)
- [pandas .at versus .loc](https://stackoverflow.com/questions/37216485/pandas-at-versus-loc)

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
df = df[df['code'].isin([...])]
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


## 布尔索引的问题

有时候通过`df = df[(df['code'].str.startswith('*ST')) & (df['code'].str.find('500') != -1])`的方式不一定找得到匹配的行，可能原因：

- 原始数据里面有无效值`NaN`，然后使用`df['code'].str.find('500') != -1]`也会返回`True`因为对于`NaN`来说也是成立的：调用find()返回NaN，NaN != -1成立。

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
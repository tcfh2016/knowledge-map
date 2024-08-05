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

- [](https://stackoverflow.com/questions/21441259/pandas-groupby-range-of-values)


## 遍历

1.简单遍历

对于Series, Dataframe的遍历操作如下：

```
for c in ufo.city:
  print(c)

for index, row in ufo.interrows():
  print(index, row.City, row.State) # 打印City, State

```

2.通过多列的值来进行行选取操作

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
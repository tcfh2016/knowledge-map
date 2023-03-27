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

## 第一个问题：怎么知道某列有哪些值？

可以使用`unique()`函数，如`dataframe["column"].unique()`。然后，我们就可以通过条件选择来过滤，从而将一个DataFrame拆分为多个DataFrame。

参考：

- [What is the unique function in pandas?](https://www.educative.io/answers/what-is-the-unique-function-in-pandas)


## 第二个问题：怎样按照值的范围进行拆分？

参考：

- [](https://stackoverflow.com/questions/21441259/pandas-groupby-range-of-values)


## min()/max()


## idxmin()/idxmax()

`idxmax()`和`idxmin`这两个函数用来返回最大值、最小值的索引，先看这两个函数的释义：

- [pandas.DataFrame.idxmax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html)

> Return index of first occurrence of maximum over requested axis.

- [pandas.DataFrame.idxmin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmin.html)

> Return index of first occurrence of minimum over requested axis.
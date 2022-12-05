
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


## 怎么判断一个单元格是否存在呢？

直接通过字符串索引去找：`row in df.index.values and col in df.columns.values`。


## 按照某列是否包含特定字符串

在pandas里面如果要使用字符串来过滤特定的行，那么必须要使用`.str`属性才可以：

```
df = df[df['code'].str.startswith('*ST')]
df = df[df['code'].str.find('500') != -1]
```

如何附加多个条件？使用逻辑表达式即可。如`df = df[df['code'].str.startswith('*ST') & df['code'].str.find('500') != -1]`。
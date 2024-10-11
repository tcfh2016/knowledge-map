## 覆写`index`

```
df.index = my_list
df.index = df['日期'] # 之前的'日期'列依然存在
```

## `set_index`：将特定列设为索引

DataFrame的 set_index方法会将其一个或多个列转换为索引，并创建一个新的 DataFrame。默认情况下那些列会从 DataFrame中移除，但也可以将其保留下来。


将如下数据的day作为新的index如何处理？

```
   code         day          pe_ratio  pb_ratio
4  601318.XSHG  2019-12-23    9.7785    2.4031
3  601318.XSHG  2019-12-24    9.7982    2.4079
2  601318.XSHG  2019-12-25    9.7368    2.3928
1  601318.XSHG  2019-12-26    9.7948    2.4071
0  601318.XSHG  2019-12-27    9.8284    2.4153
```

直接使用`set_index`重设索引之后并不会在原来的DataFrame里面改动生效。该函数默认参数`drop=True`，如果像保留之前的列可将其设置为`False`。

```
df.set_index('day')
```

*注1：DataFrame的set_index函数会将一个或多个列转换为行索引，并创建新的DataFrame。*
*注2：Index 对象是不可修改的。因此df.index[1] = 'c'会提示错误。*

参考：

- [Remove index name in pandas](https://stackoverflow.com/questions/29765548/remove-index-name-in-pandas)



## `reset_index`：刷新索引

reset_index方法的作用与 set_index相反，层次化索引被转话为具体列，新的索引默认以0~N的整数索引替代。

可以使用`reset_index`刷新DataFrame的索引。带上`drop=True`参数就不会保留原来的索引，否则会保留：

```
    a   b   c
4  30  30   0
1  10  10  10
2  20  20  20
3  40  40  40

# 不带drop=True的参数
 index   a   b   c
0      4  30  30   0
1      1  10  10  10
2      2  20  20  20
3      3  40  40  40
```

参考：

- [How to reset index in a pandas dataframe?](https://stackoverflow.com/questions/20490274/how-to-reset-index-in-a-pandas-dataframe)

## `reindex`：重设索引

DataFrame 最初的数据与创建时指定的 index顺序密切相关，通过 reindex方法可以创建一个适应新索引的新对象。在使用 reindex()方法时可以指定一些额外选项，比如 fill_value=0 表示对于其中的 NaN的值全填写为 0。

```
obj = Series([4.2, 2.3, -1.3, 5.2], index=['d', 'b', 'c', 'a'])

obj1 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
obj3 = obj.reindex(['a', 'b', 'c', 'd', 'e'], method='ffill')
obj4 = obj.reindex(['a', 'b', 'c', 'd', 'e'], method='bfill')
```

## 获取索引为 list

在[Get row-index values of Pandas DataFrame as list? [duplicate]](https://stackoverflow.com/questions/18358938/get-row-index-values-of-pandas-dataframe-as-list)找到了答案：

```
df.index.values.tolist() #ndarray
list(df.index.values)
```

## 按列值获取对应的行索引

```
df.index[df['column_name']==value].tolist()
```

参考：

- [Pandas: Get Index of Rows Whose Column Matches Value](https://www.statology.org/pandas-get-index-of-row/)


## 层次化索引

层次化索引使你可以在一个轴上拥有多个（两个以上）索引级别，让你能够以低纬度形式处理高维度数据。


```
#选择第一层索引为“bar”，第二层索引为“two”的这一行
df.loc[("bar", "two")] 

#选择第一层索引为“bar”，第二层索引为“two”的这一行，第“A”列的单元格
df.loc[("bar", "two"), "A"] 

# 选择第一层索引为“bar”的所有元素
df.loc["bar"]

```

## 日期索引

```
di = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(di)), di)

ts_utc = ts.tz_localize('UTC') # 标准时间
ts_utc.tz_convert('US/Eastern') # 改变时区
```

## 参考

- [Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-and-selecting-data)
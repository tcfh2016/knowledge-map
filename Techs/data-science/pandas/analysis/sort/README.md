## 排序

使用`sort_values()`进行排序，并指定排序的列名，默认按照“升序”

```
df.sort_values(by=[column]) # 默认升序
df.sort_values(by=[column], ascending=False) # 默认升序
```

按照多行排序：

```
df.sort_values(by=[column1, column2], ascending=False) # 默认升序
```


## sort_values()

对某列的series进行排序：

```
movies['title'].sort_values() # 默认以升序排列
movies['title'].sort_values(ascending=False) # 以降序排列
```

对整个dataframe以某列为标准进行排序：

```
movies.sort_values('title') # 升序排列，不会更改原有dataframe
movies.sort_values('title', ascending=False) # 降序排列，不会更改原有dataframe
movies.sort_values(['content_rating', 'duration']) # 以两列进行排序
```

## 仅仅针对前面N行排序

先部分排序，再拼接起来：

```
pd.concat([df[0:N].sort_values('A'), df[N:]])
```


## 将数据按照时间顺序颠倒过来

```
   code         day  pe_ratio  pb_ratio
0  601318.XSHG  2019-12-27    9.8284    2.4153
1  601318.XSHG  2019-12-26    9.7948    2.4071
2  601318.XSHG  2019-12-25    9.7368    2.3928
3  601318.XSHG  2019-12-24    9.7982    2.4079
4  601318.XSHG  2019-12-23    9.7785    2.4031
```

DataFrame提供了`sort_index()`和`sort_value`分别按照索引和值排序：

```
df1 = frame.sort_values(axis=0, by="clumn_name",ascending=False)
```

## `rank()`

排序时如果碰到了相同的元素，那么该怎么排呢？这个时候就需要使用到`rank(method = "first", ascending=False)`：

- `average`：默认值，平均排名
- `min`：最小值排名
- `max`：最大值排名
- `first`：原始数据中出现的顺序来排
- `dense`：密集排名


## 参考

- [How to Sort Pandas DataFrame (with examples)](https://datatofish.com/sort-pandas-dataframe/)
- [Pandas Sort: Your Guide to Sorting Data in Python](https://realpython.com/pandas-sort-python/)




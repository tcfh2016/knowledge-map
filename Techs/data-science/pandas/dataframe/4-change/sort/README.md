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


## 参考

- [How to Sort Pandas DataFrame (with examples)](https://datatofish.com/sort-pandas-dataframe/)
- [Pandas Sort: Your Guide to Sorting Data in Python](https://realpython.com/pandas-sort-python/)


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

2.`rank()`

参考：

- [关于pandas的rank()函数的一点认识](https://zhuanlan.zhihu.com/p/87593543)

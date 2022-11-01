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
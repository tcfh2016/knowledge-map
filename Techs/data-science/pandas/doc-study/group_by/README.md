## [分组/Group by](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)

"group by"通常涉及以下一个或多个操作：

- 根据标准将数据分为多组
- 针对每组应用某种函数（统计、转换、过滤）
- 将所有的结果联合成某种数据结构

## 将对象进行分组

进行分组的时候默认的axis为0，对象可以根据不同的轴进行分组，使用的语法格式为`obj.groupby(key)`, `obj.groupby(key, axis=1)`, `obj.groupby(key1, key2)`。

分组之后的结果为`DataFrameGroupBy`对象，这种对象是一种按照分组组织起来的形式，是无法直接打印的，可以通过其他方法来打印出其中的部分数据：

- `grouped.first()`：打印出所有group里的第一项记录
- `grouped.get_group('bird')`：打印出特定group里的所有记录

另外可以遍历打印所有group的数据：

```
grouped = df.groupby('class')
for name, group in grouped:
    print(name)
    print(group)
```

参考：

- [Pandas GroupBy](https://www.geeksforgeeks.org/pandas-groupby/)
- [Python | Pandas dataframe.groupby()](https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/)
- [](https://zhuanlan.zhihu.com/p/101284491)

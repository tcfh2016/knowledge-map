## [dataframe.()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)

`dataframe.rolling()`用来完成滑动窗口计算，这种计算常用在信号处理和时间序列数据的分析。在计算的时候一次性计算多个连续的值（确定窗口大小，确定数据操作）。

```
DataFrame.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=_NoDefault.no_default, closed=None, step=None, method='single')
```

如果要使用自定义的函数，可以使用`apply`：

```
pd.Series(arr).rolling(6, min_periods=1).apply(my_func)
```

参考：

- [用pandas中的rolling函数计算时间窗口数据](https://baijiahao.baidu.com/s?id=1622798772654712959&wfr=spider&for=pc)
- [Python | Pandas dataframe.rolling()](https://www.geeksforgeeks.org/python-pandas-dataframe-rolling/)

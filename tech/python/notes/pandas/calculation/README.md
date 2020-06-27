# 常用函数

## div()

和NumPy数组一样，DataFrame和Series之间算术运算会以“广播(broadcasting)”的形式进行，且
默认将Series的索引匹配到DataFrame的列，然后沿着行一直向下广播，也就是说以行为单位求取所
有行的运算值。

如果要匹配行且在列上进行广播，需要在调用算术运算函数时指定匹配的坐标轴，即 axis=0。

```
percent_items = percent_items[:].div(percent_items['营业收入(万元)'], axis=0)
```

## sort_values()

对某列的series进行排序：

```
movies.title.order # 旧的排序方法，已经弃用。

movies.title.sort_values()
movies['title'].sort_values() # 默认以升序排列
movies['title'].sort_values(ascending=False) # 以降序排列
```

对整个dataframe以某列为标准进行排序：

```
movies.order('title') # 旧的排序方法，已经弃用。

movies.sort_values('title') # 升序排列，不会更改原有dataframe
movies.sort_values('title', ascending=False) # 降序排列，不会更改原有dataframe
movies.sort_values(['content_rating', 'duration']) # 以两列进行排序
```

## map(f)/applymap(f)

map作用于 Series，applymap作用于 DataFrame，表示对每个元素应用函数f。

## pct_change()

这个函数是用来计算行与行之间的数值变动，以百分比表示，默认计算相对于前一行的变化情况。比如：

```
             A   B   C   D
2000-01-02  14   5  20  14
2000-01-09   4   2  20   3
2000-01-16   5  54   7   6
2000-01-23   4   3  21   2
2000-01-30   1   2   8   6
2000-02-06  55  32   5   4

                    A          B         C         D
2000-01-02        NaN        NaN       NaN       NaN
2000-01-09  -0.714286  -0.600000  0.000000 -0.785714
2000-01-16   0.250000  26.000000 -0.650000  1.000000
2000-01-23  -0.200000  -0.944444  2.000000 -0.666667
2000-01-30  -0.750000  -0.333333 -0.619048  2.000000
2000-02-06  54.000000  15.000000 -0.375000 -0.333333
```

如果我们要计算每行相对于前面第2行的变动情况，那么只需要执行`df.pct_change(2)`即可：

```
                    A         B         C         D
2000-01-02        NaN       NaN       NaN       NaN
2000-01-09        NaN       NaN       NaN       NaN
2000-01-16  -0.642857  9.800000 -0.650000 -0.571429
2000-01-23   0.000000  0.500000  0.050000 -0.333333
2000-01-30  -0.800000 -0.962963  0.142857  0.000000
2000-02-06  12.750000  9.666667 -0.761905  1.000000
```

参考：

- [Python | Pandas dataframe.pct_change()](https://www.geeksforgeeks.org/python-pandas-dataframe-pct_change/)
- [pandas.DataFrame.pct_change](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pct_change.html)


## [dataframe.rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html)

`dataframe.rolling()`用来完成滑动窗口计算，这种计算常用在信号处理和时间序列数据的分析。在计算的时候一次性计算多个连续的值（确定窗口大小，确定数据操作）。

参考：

- [用pandas中的rolling函数计算时间窗口数据](https://baijiahao.baidu.com/s?id=1622798772654712959&wfr=spider&for=pc)
- [Python | Pandas dataframe.rolling()](https://www.geeksforgeeks.org/python-pandas-dataframe-rolling/)

## div()

和NumPy数组一样，DataFrame和Series之间算术运算会以“广播(broadcasting)”的形式进行，且默认将Series的索引匹配到DataFrame的列，然后沿着行一直向下广播，也就是说以行为单位求取所有行的运算值。

如果要匹配行且在列上进行广播，需要在调用算术运算函数时指定匹配的坐标轴，即 axis=0。

```
percent_items = percent_items[:].div(percent_items['营业收入(万元)'], axis=0)
```

参考：

- [Python | Pandas dataframe.div()](https://www.geeksforgeeks.org/python-pandas-dataframe-div/)
## 打印Dataframe的时候使用to_string()作用？

如果不用`to_string()`那么行数较多的时候会隐藏：只显示开头和尾部的5行数据，但是使用了这个方法之后可以全部输出。

最大的显示行是由`pd.options.display.max_rows`和`pd.options.display.min_rows`来控制的，前者默认为60，后者默认为10。所以你可以调整这两个参数来进行设置。它们之间的规则是：

- 如果max_rows足以显示整个df的行数，那么显示所有的行
- 如果max_rows不足以显示整个df的行数，那么显示min_rows行


## ValueError: could not convert string to float

`ValueError: could not convert string to float`错误可能因为获取到的dataframe里面有些是空的，所以无法将对应值转换为float。


- [Decimal place issues with floats and decimal.Decimal](https://stackoverflow.com/questions/286061/decimal-place-issues-with-floats-and-decimal-decimal)
- [How to do Decimal to float conversion in Python?](https://stackoverflow.com/questions/32285927/how-to-do-decimal-to-float-conversion-in-python)

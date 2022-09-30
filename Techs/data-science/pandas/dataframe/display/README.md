## 输出排版

打印DataFrame输出的格式有些时候并不友好，比如：

![](print_not_aligned.png)


## 打印Dataframe的时候使用to_string()作用？

如果不用`to_string()`那么行数较多的时候会隐藏：只显示开头和尾部的5行数据，但是使用了这个方法之后可以全部输出。

最大的显示行是由`pd.options.display.max_rows`和`pd.options.display.min_rows`来控制的，前者默认为60，后者默认为10。所以你可以调整这两个参数来进行设置。它们之间的规则是：

- 如果max_rows足以显示整个df的行数，那么显示所有的行
- 如果max_rows不足以显示整个df的行数，那么显示min_rows行


## print的时候如何显示更多列或者行？

```
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
```

## print的时候数值太大无法全部展示？

比如下面的time，其实暗含了日期和时间，但是由于是float格式默认按照科学计数法显示了，如何将其全部显示出来？

```
           time  current   high    low       volume         money
0  2.020021e+13    1.987  2.022  1.965  338313044.0  6.753016e+08
0  2.020022e+13    2.071  2.071  2.004  689679516.0  1.411302e+09
0  2.020022e+13    2.090  2.090  2.050  704272926.0  1.461049e+09
0  2.020022e+13    2.054  2.087  2.052  572403776.0  1.184645e+09
```

可以通过`pd.set_option('display.float_format', lambda x: '%.2f' % x)`取消默认的科学计数法，另外可以通过`pd.set_option(‘precision’, n)`显示小数点。

参考：

- [How do I expand the output display to see more columns of a pandas DataFrame?](https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe)



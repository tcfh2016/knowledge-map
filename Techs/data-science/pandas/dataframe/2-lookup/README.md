## 数据类型

可以通过`df.dtypes`查看各列的类型，通过`df.info()`函数可以查看更详细的内容。

`df.dtypes`的输出：

```
class      object
math        int32
physics     int32
dtype: object
```

`df.info()`的输出：

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   class    2 non-null      object
 1   math     2 non-null      int32 
 2   physics  2 non-null      int32 
dtypes: int32(2), object(1)
memory usage: 160.0+ bytes
None
```

使用`df = df.convert_dtypes()`进行快速数据类型转换。


## 显示更多列/行

在打印出DataFrame时最大的显示行由`pd.options.display.max_rows`和`pd.options.display.min_rows`来控制的，前者默认为60，后者默认为10。它们之间的规则是：

- 如果max_rows足以显示整个df的行数，那么显示所有的行。
- 如果max_rows不足以显示整个df的行数，那么显示min_rows行。

你可以调整这两个参数：

```
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
```

也可以使用`to_string()`来全部输出整个DataFrame的内容。


## 取消科学计数法的格式

比如下面的time，其实暗含了日期和时间，但是由于是float格式默认按照科学计数法显示了，如何将其全部显示出来？

```
           time  current   high    low       volume         money
0  2.020021e+13    1.987  2.022  1.965  338313044.0  6.753016e+08
0  2.020022e+13    2.071  2.071  2.004  689679516.0  1.411302e+09
0  2.020022e+13    2.090  2.090  2.050  704272926.0  1.461049e+09
0  2.020022e+13    2.054  2.087  2.052  572403776.0  1.184645e+09
```

可以通过如下设置来将DataFrame的展示方式替换为浮点数且保留两位小数，也就取消了默认的科学计数法展示格式。

```
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.float_format', "{:.2f}".format)
pd.set_option('precision', 2)
```

参考：

- [How do I expand the output display to see more columns of a pandas DataFrame?](https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe)


## 输出排版

打印DataFrame输出的格式有些时候并不友好，比如：

![](print_not_aligned.png)





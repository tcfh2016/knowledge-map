## Analyzing Data

最为常用的查看DataFrame的方法是`head(c)`/`tail(c)`，使用它你可以查看一个DataFrame的前面c行或者末尾c行。如果不指定c，那么打印的行数默认为5行。

使用`info()`可以打印出对应DataFrame的基本信息，下面是打印出的一个DataFrame的例子：

```
<class 'pandas.core.frame.DataFrame'>
  RangeIndex: 169 entries, 0 to 168
  Data columns (total 4 columns):
   #   Column    Non-Null Count  Dtype  
  ---  ------    --------------  -----  
   0   Duration  169 non-null    int64  
   1   Pulse     169 non-null    int64  
   2   Maxpulse  169 non-null    int64  
   3   Calories  164 non-null    float64
  dtypes: float64(1), int64(3)
  memory usage: 5.4 KB
  None
```

上面的信息告诉了我们该DataFrame的行列数、每列数据的类型，以及有每列可能存在的空值的个数。这些空值在进行数据分析的时候是需要清理的。

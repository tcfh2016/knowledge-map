# 日期数据

## 日期序列

```
pandas.date_range(start=None, end=None, periods=None, freq=None)
```

常见的`freq`有`min`(minutely frequency)、`s`(secondly frequency)、`ms`(milliseconds)。


参考：

- [pandas.date_range](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html)


## 格式转换

日期格式有各种各样的类型，Pandas提供了`to_datetime()`来将不同类型的日期格式统一起来。

```
pandas.to_datetime(arg, dayfirst=False, yearfirst=False, utc=None, format=None, unit=None)
```

使用`to_datetime()`进行转换之后的对象类型为`Timestamp`。


# 时间序列


## 重采样：`resample`

对于时间序列从一个频率转换到另一个频率的调整过程，比如将每天转换为每5天，称为“重采样”。

```
df.resample(rule, how=None, axis=0, fill_method=None, closed='left')
```

## 降采样

采样的周期由高频率变为低频率，数据降采样会涉及到数据的聚合（求和，均值等），比如`s.resample('3min').sum()`是将一个series按照3分钟重采样并求和，类似于按照3分钟进行分组之后求和。


## 升采样

采样的周期由低频率变为高频率，不需要数据的聚合，相反需要涉及到数据的填充。常用三种填充方法：

1. 不填充
2. 前值填充：`ffill`
3. 后值填充：`bfill`


## `ohlc()`

金融领域经常需要查看开盘、收盘、最高价、最低价的数据，经过重采样的数据使用`ohlc()`函数可以轻松得到这样的数据。


## 移动窗口：`rolling()`

重采样可以得到任何频率的数据，通过移动窗口可以基于每个时间点考虑一段时间的数据，用区间的概念来处理数据。

移动平均窗口能够让数据变得更加平滑。

```
df.rolling(window, min_periods=None, axis=0, closed=None)
```

这里`min_periods`没有设置的时候，当观察的数量小于指定的`window`设置的数量时就为`NaN`。
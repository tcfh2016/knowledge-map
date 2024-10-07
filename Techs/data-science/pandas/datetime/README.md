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
df.resample(rule, how=None, axis=0, fill_method=None)
```

比如`s.resample('3min').sum()`是将一个series按照3分钟重采样并求和，类似于按照3分钟进行分组之后求和。
## [Time series / date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)

Pandas基于Numpy的datetime64, timedelta64对象提供了很多操作时间序列的功能。比如：

```
# 生成时间序列，
dti = pd.date_range('2018-01-01', periods=3, freq='H')
# 输出：
# DatetimeIndex(['2018-01-01 00:00:00', '2018-01-01 01:00:00',
#                '2018-01-01 02:00:00'],
#                dtype='datetime64[ns]', freq='H')

# 时区转换
dti.tz_localize('UTC')
dti.tz_convert('US/Pacific')
```

同时，Pandas提供了四个与时间相关的概念：

- Date times，特定的日期数据，提供时区支持，与标准库中的`datetime.datetime`类似。
- Time deltas，绝对时间间隔，与标准库中的`datetime.timedelta`类似。
- Time spans，由某个时间点开始且周期性跳跃的时间跨度。
- Date offsets，相对的时间偏移量，类似于dateutil包中的`dateutil.relativedelta.relativedelta`。

|Concept|Scalar Class|Array Class|pandas Data Type|Primary Creation Method|
|-|-|-|-|-|
|Date times|Timestamp|DatetimeIndex|datetime64[ns] or datetime64[ns,tz]|to_datetime or date_range|
|Time deltas|Timedelta|TimedeltaIndex|timedelta64[ns]|to_timedelta or timedelta_range|
|Time spans|Period|PeriodIndex|period[freq]|Period or period_range|
|Date offsets|DateOffset|None|None|DateOffset|

时间序列数据通常作为Series或DataFrame的index使用。时间为空的时候pandas里面用NaT表示，类似于np.nan来表示浮点数值。


## 如何获取将`Timestamp`转化为`datetime.date`？

`Timestamp`本身是一个复合类型

```
In [11]: t = pd.Timestamp('2013-12-25 00:00:00')

In [12]: t.date()
Out[12]: datetime.date(2013, 12, 25)

In [13]: t.date() == datetime.date(2013, 12, 25)
Out[13]: True

```

参考：

- [Pandas: Convert Timestamp to datetime.date](https://stackoverflow.com/questions/34386751/pandas-convert-timestamp-to-datetime-date)


## date_range 和 period_range

```
In [21]: pd.Series(pd.period_range('1/1/2011', freq='M', periods=3))
Out[21]:
0    2011-01
1    2011-02
2    2011-03


In [23]: pd.Series(pd.date_range('1/1/2011', freq='M', periods=3))
Out[23]:
0   2011-01-31
1   2011-02-28
2   2011-03-31
```


## Timestamps vs Time Spans

Timestamps/Time Span都可以用来做为index，前者表示具体的时间点（DatetimeIndex类型），后者表示时间间隔（PeriodIndex类型）。

```
time_stamp = pd.Timestamp(datetime.datetime(2012, 5, 1))
# 2012-05-01 00:00:00
time_stamp = pd.Timestamp('2012-05-01')
# 2012-05-01 00:00:00

# 以Timestamp做为index
dates = [pd.Timestamp('2012-05-01'),
         pd.Timestamp('2012-05-02'),
         pd.Timestamp('2012-05-03')]
ts = pd.Series(np.random.randn(3), dates)
#2012-05-01   -1.863204
#2012-05-02    1.337686
#2012-05-03    0.173678
# 当timestamp做为pandas的index的时候，Timestamp/Period 类型自动转换为 DatetimeIndex/
# PeriodIndex 类型，但为啥这个时候不会有时分秒的表示？

# 以Period做为index
periods = [pd.Period('2012-01'), pd.Period('2012-02'), pd.Period('2012-03')]
ts = pd.Series(np.random.randn(3), periods)
```


## 转换为 Timestamps

使用`to_datetime()`可以将诸如字符串、epochs或者复合类型的时间对象转换为 dtetime64。可以单独转换，也可以批量转换。

批量转换返回的是DatetimeIndex，该对象的主要用处之一是对pandas对象做索引，它包括了普通index对象的所有功能，同时还提供了针对时间的特别处理。

```
# 转换列表
pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]))

输出:
0   2009-07-31
1   2010-01-10
2          NaT
dtype: datetime64[ns]

# 转换单个字符串
pd.to_datetime('2010/11/12')
输出: Timestamp('2010-11-12 00:00:00')

pd.Timestamp('2010/11/12')
输出: Timestamp('2010-11-12 00:00:00')
```

## 生成 timestamp 区间

生成 timestamp 区间通常可以使用两个方法：[date_range()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html#pandas.date_range)或者[bdate_range()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.bdate_range.html#pandas.bdate_range)，前者默认日历日，后者默认为工作日。

```
start = datetime.datetime(2011, 1, 1)
end = datetime.datetime(2012, 1, 1)

calendar_index = pd.date_range(start, end)  # 包含所有日历天数
business_index = pd.bdate_range(start, end) # 去除了区间内的非工作日
```

除了上面这种最简单的方式，date_range()还支持通过start, end, periods, 和freq来生成多样化的日期。

```
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
pd.date_range(start, periods=1000, freq='M')   # month end frequency
pd.date_range(start, periods=1000, freq='MS')  # month start frequency
pd.bdate_range(start, periods=250, freq='BQS') # business quarter end frequency
pd.date_range(start, end, freq='BM') # business month end
pd.date_range(start, end, freq='W')  # weekly frequency
```


## 如何判断Timestamp类型

```
print(isinstance(d, pd.Timestamp))
```

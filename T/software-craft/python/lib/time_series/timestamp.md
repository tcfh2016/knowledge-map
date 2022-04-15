# [Time series / date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)

Pandas基于Numpy的datetime64,timedelta64对象提供了很多操作时间序列的功能。比如：

```
import datetime

# 根据不同的类型转化为日期格式
# 1. 字符串格式"1/1/2018", "2018-01-01"
# 2. numpy.datetime64 类型
# 3. datetime.datetime 类型
dti = pd.to_datetime(['1/1/2018', np.datetime64('2018-01-01'), datetime.datetime(2018, 1, 1)])

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

上面的代码里面出现了三种不同的日期格式：字符串、numpy.datetime64和datetime.datetime类
型。

- 字符串是一种最简单的表示形式常用来做为日期的输入，因为不同国家使用不同的日期格式，所以
定义了专门的时间表示标准ISO 8601来统一日期输入，格式为“YYYY-MM-DD hh:mm:ss.ms”或者
“YYYY-MM-DDThh:mm:ss.ms”(numpy的输出使用后一种格式)。但它无法提供基于日期/时间的很多功
能，比如：
  - 获取某个月到底有多少天
  - 2019年3月1日下午1点到2019年3月4日上午2年有多少秒
  - 1970年1月1日到2008年12月3日有多少个工作日
- numpy.datetime64是以64位的数据来保存日期，其中包含Y, M, W, D, h, m, s, ms, us。一
些常见的日期运算包括：
  - np.datetime64('2000-11-27') + 2：按天相加的结果为2000-11-29，numpy自动识别日期类
  型
  - np.datetime64('2000-11') + 2：按天相加的结果为2001-01，numpy自动识别日期类
  型
  - some_date + np.timedelta64(4, 'M') + np.timedelta64(3, 'D')：使用timedelta64
  对象
- datetime 是Python内建的日期/时间处理模块，里面包括了date/time/datetime/timedelta/
tzinfo/timezone六种对象。
  - date用来处理日期，初始化必须分别传入年、月、日进行初始化
    - today=date.today()/today.year/today.month/today.day
  - time用来处理时钟，时间的初始化类似也要分别传入时分秒等参数，但它们都是可选的
    - time=time(12,34,56)/time.hour/time.minute/time.second/time.microsecond
  - datetime是date/time对象的结合体
    - now=datetime.now()
  - timedelta是用来计算日期差距的对象

参考：

- [numpy.datetime64() method](https://www.geeksforgeeks.org/python-numpy-datetime64-method/)
- [NumPy Datetime: How to Work with Dates and Times in Python?](https://blog.finxter.com/how-to-work-with-dates-and-times-in-python/)
- [Python datetime module with examples](https://www.geeksforgeeks.org/python-datetime-module-with-examples/)
- [Converting between datetime, Timestamp and datetime64](https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64)

在[Converting between datetime, Timestamp and datetime64](https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64/46921593#46921593)这里提到了datetime/numpy.datetime64/pd.Timestamp的区别。

- datetime 是Python提供的处理日期/时间的标准库，日期和时间由不同的对象表示。
- numpy提供的 datatime64/timedelta64对象是不同的库，它支持毫秒级别的精度，并且用同一个
对象来处理日期/时间。
- pandas提供的 Timestamp/Timedelta基于numpy提供了更为多样化功能。

## 概览

Pandas提供了四个与时间相关的概念：

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

时间序列数据通常作为Series或DataFrame的index使用。时间为空的时候pandas里面用NaT表示，
类似于np.nan来表示浮点数值。

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

Timestamps/Time Span都可以用来做为index，前者表示具体的时间点（DatetimeIndex类型），
后者表示时间间隔（PeriodIndex类型）。

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

使用`to_datetime()`可以将诸如字符串、epochs或者复合类型的时间对象转换为 dtetime64，如
果有多个元素那么返回的类型则为 DatetimeIndex。

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

除了上面这种最简单的方式，date_range()还支持通过start, end, periods, 和freq来生成多样
化的日期。

```
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
pd.date_range(start, periods=1000, freq='M')   # month end frequency
pd.date_range(start, periods=1000, freq='MS')  # month start frequency
pd.bdate_range(start, periods=250, freq='BQS') # business quarter end frequency
pd.date_range(start, end, freq='BM') # business month end
pd.date_range(start, end, freq='W')  # weekly frequency
```

## 索引

DatetimeIndex 对象的主要用处之一是对pandas对象做索引，它包括了普通index对象的所有功能，
同时还提供了针对时间的特别处理。

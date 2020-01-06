# [Time series / date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)

Pandas提供了很多操作时间序列的功能。比如：

```
import datetime

# 根据不同的类型转化为日期格式
dti = pd.to_datetime(['1/1/2018', np.datetime64('2018-01-01'), datetime.datetime(2018, 1, 1)])

# 生成时间序列
dti = pd.date_range('2018-01-01', periods=3, freq='H')

# 时区转换
dti.tz_localize('UTC')
dti.tz_convert('US/Pacific')
```

## 概览

Pandas提供了四个与时间相关的概念：

- Date times，特定的日期数据，提供时区支持，与标准库中的`datetime.datetime`类似。
- Time deltas，绝对时间间隔，与标准库中的`datetime.timedelta`类似。
- Time spans，由某个时间点开始且周期性跳跃的时间跨度。
- Date offsets，相对的时间偏移量，类似于dateutil包中的`dateutil.relativedelta.relativedelta`。

时间序列数据通常做为Series或DataFrame的index使用。

## Timestamps vs Time Spans

Timestamps/Time Span都可以用来做为index，前者表示具体的时间点（DatetimeIndex类型），
后者表示时间间隔（PeriodIndex类型）。

```
# 以Timestamp做为index
dates = [pd.Timestamp('2012-05-01'),
         pd.Timestamp('2012-05-02'),
         pd.Timestamp('2012-05-03')]
ts = pd.Series(np.random.randn(3), dates)


# 以Period做为index
periods = [pd.Period('2012-01'), pd.Period('2012-02'), pd.Period('2012-03')]
ts = pd.Series(np.random.randn(3), periods)
```

## 转换为 Timestamps

使用`to_datetime()`可以将Series或者列表转换为 Timestamp，如果仅有一个元素转为的类型为
Timestamp，如果有多个元素那么返回的类型则为 DatetimeIndex。

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

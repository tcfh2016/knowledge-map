# datetime

datetime 是Python内建的日期/时间处理模块，里面包括了date/time/datetime/timedelta/
tzinfo/timezone六种对象。

- date用来处理日期，初始化必须分别传入年、月、日进行初始化
  - today=date.today()/today.year/today.month/today.day
- time用来处理时钟，时间的初始化类似也要分别传入时分秒等参数，但它们都是可选的
  - time=time(12,34,56)/time.hour/time.minute/time.second/time.microsecond
- datetime是date/time对象的结合体
  - now=datetime.now()
- timedelta是用来计算日期差距的对象

参考：

- [Python datetime module with examples](https://www.geeksforgeeks.org/python-datetime-module-with-examples/)


## `datetime.date`和字符串之间的转换

创建 `datetime.date`时必须分别给与年、月、日的参数，所以字符串必须要进行拆分。

```
# 方式一

datetime.date
import time, datetime

date_str = '2017-10-19'
fmt = '%Y-%m-%d'
time_tuple = time.strptime(date_str, fmt)
year, month, day = time_tuple[:3]
date = datetime.date(year, month, day)

# 方式二
import datetime

date_str = '2017-10-19'
print(datetime.date(*map(int, date_str.split('-'))))
```

## 如何将`datetime.date`类型的数据增加一天

```
date2 + datetime.timedelta(days=35)
```

# 初始化

date, time, datetime, timedelta对应着不同的初始化方式。

```
year = int(date_split_list[0])
month = int(date_split_list[1])
day = int(date_split_list[2])

now = datetime(year, month, day)
```

# 常见问题

## 如何获得今天的日期 ？

获取日期需要使用日期对象`date`，可以通过`datetime.date.today()`获得今天的日期。注意，
这个时候是不包括时间的。

## 如何获取将`Timestamp`转化为`datetime.date`？

```
In [11]: t = pd.Timestamp('2013-12-25 00:00:00')

In [12]: t.date()
Out[12]: datetime.date(2013, 12, 25)

In [13]: t.date() == datetime.date(2013, 12, 25)
Out[13]: True

```

参考：

- [Pandas: Convert Timestamp to datetime.date](https://stackoverflow.com/questions/34386751/pandas-convert-timestamp-to-datetime-date)


## 如何将`numpy.float64`转换为时间类型？

`20180702210000`这种格式实际上指明了时间，但是是`float`类型，怎么样将其显示出来？

```
[(20180702210000.0, 272.9, 272.95, 272.9, 492.0, 134285000.0)
 (20180702210001.0, 272.85, 272.95, 272.85, 884.0, 241270200.0)
 (20180702210001.5, 272.9, 272.95, 272.85, 1280.0, 349320300.0) ...
 (20180703145958.5, 271.9, 272.95, 271.3, 123526.0, 33623516800.0)
 (20180703145959.0, 271.85, 272.95, 271.3, 123528.0, 33624060500.0)
 (20180703150000.0, 271.9, 272.95, 271.3, 123536.0, 33626235700.0)]
```

## 如何判断Timestamp类型

```
print(isinstance(d, pd.Timestamp))
```

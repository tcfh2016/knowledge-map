## Python中的时间类型

[Converting between datetime, Timestamp and datetime64](https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64/46921593#46921593)提到了datetime/numpy.datetime64/pd.Timestamp的区别。

- datetime 是Python提供的处理日期/时间的标准库，日期和时间由不同的对象表示。
- numpy提供的 datatime64/timedelta64对象是不同的库，它支持毫秒级别的精度，并且用同一个对象来处理日期/时间。
- pandas提供的 Timestamp/Timedelta基于numpy提供了更为多样化功能。


## 时间表示方式

常见的日期格式有字符串、numpy.datetime64和datetime.datetime类型。

1，字符串

字符串是一种最简单的表示形式常用来做为日期的输入，因为不同国家使用不同的日期格式，所以定义了专门的时间表示标准ISO 8601来统一日期输入，格式为“YYYY-MM-DD hh:mm:ss.ms”或者“YYYY-MM-DDThh:mm:ss.ms”(numpy的输出使用后一种格式)。但它无法提供基于日期/时间的很多功能，比如：

- 获取某个月到底有多少天
- 2019年3月1日下午1点到2019年3月4日上午2年有多少秒
- 1970年1月1日到2008年12月3日有多少个工作日

2，numpy.datetime64

numpy.datetime64是以64位的数据来保存日期，其中包含Y, M, W, D, h, m, s, ms, us。一些常见的日期运算包括：
- np.datetime64('2000-11-27') + 2：按天相加的结果为2000-11-29，numpy自动识别日期类型
- np.datetime64('2000-11') + 2：按天相加的结果为2001-01，numpy自动识别日期类型
- some_date + np.timedelta64(4, 'M') + np.timedelta64(3, 'D')：使用timedelta64对象

3，datetime

datetime是Python内建的日期/时间处理模块，里面包括了date/time/datetime/timedelta/tzinfo/timezone六种对象。

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

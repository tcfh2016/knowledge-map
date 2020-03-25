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

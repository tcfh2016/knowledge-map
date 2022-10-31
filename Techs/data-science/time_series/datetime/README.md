## datetime是什么？

`datetime`是Python内建的日期/时间处理模块，里面包括了date/time/datetime/timedelta/tzinfo/timezone六种对象。

- datetime是date/time对象的结合体，既有日期的信息，又有时间的信息
  - dt = datetime.datetime(2019, 9, 3, 22, 5, 22, 154594)
  - now=datetime.now()
- date用来处理日期，初始化必须分别传入年、月、日进行初始化
  - dt = datetime.date(2019, 9, 3)
  - today=date.today()
  - today.year/today.month/today.day
- time用来处理时钟，时间的初始化类似也要分别传入时分秒等参数，但它们都是可选的
  - time=time(12,34,56)
  - time.hour/time.minute/time.second/time.microsecond
- timedelta是用来计算日期差距的对象

参考：

- [Python datetime module with examples](https://www.geeksforgeeks.org/python-datetime-module-with-examples/)


## 初始化

date, time, datetime, timedelta对应着不同的初始化方式。在创建 `datetime.date`时必须分别给与年、月、日的参数。可以通过`datetime.date.today()`获得今天的日期。

```
year = int(date_split_list[0])
month = int(date_split_list[1])
day = int(date_split_list[2])

now = datetime(year, month, day)
```


## 月份的日期转换

可以使用`strftime`来进行转换：


或者：

```
def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1
```

参考：

- [](https://stackoverflow.com/questions/3418050/how-to-map-month-name-to-month-number-and-vice-versa)
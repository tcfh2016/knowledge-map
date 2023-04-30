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

使用`datetime.strptime`来完成字符串到datetime类型的转换。

```
import pandas as pd
import datetime as dt

f = 20180702210001.0

fmt = '%Y%m%d%H%M%S.%f'
time_tuple = dt.datetime.strptime(str(f), fmt)
```

`strftime(format)`是干啥的？它实际上是`strptime(date_string, format)`的逆运算，用来将一个datetime对象转换为字符串类型，比如：

```
date = dt.datetime.today().date()
print(date)

fmt = '%Y%m%d'
print(date.strftime(fmt))
```

参考：

- [strftime() and strptime() Behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

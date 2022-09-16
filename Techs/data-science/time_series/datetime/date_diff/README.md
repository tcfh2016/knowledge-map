## 如何计算两个日期之间相差的天数？

```
import datetime

date = datetime.date(2020, 1, 1)
today = datetime.date.today()
diff =  today - date

print(diff.days)
```

## 如何将`datetime.date`类型的数据增加一天

```
date2 + datetime.timedelta(days=35)
```

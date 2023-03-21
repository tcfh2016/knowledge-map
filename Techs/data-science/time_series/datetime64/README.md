## datetime64

numpy.datetime64是以64位的数据来保存日期，其中包含Y, M, W, D, h, m, s, ms, us。一些常见的日期运算包括：

- np.datetime64('2000-11-27') + 2：按天相加的结果为2000-11-29，numpy自动识别日期类型
- np.datetime64('2000-11') + 2：按天相加的结果为2001-01，numpy自动识别日期类型
- some_date + np.timedelta64(4, 'M') + np.timedelta64(3, 'D')：使用timedelta64对象

比如字符串`2023-03-22`转换为`datetime64`之后为`2023-03-22 00:00:00`，也就是会在年、月、日后面接小时、分钟、秒。

## 属性


## 转换为 datetime64

可以使用`pd.to_datetime(['20230320', '20230321])`来将字符串转换为`datetime64`类型。

不过它识别的格式有限，所以有时候需要指定`format`参数来指示要转换的日期格式，比如：`pd.to_datetime(['20230320', '20230321], format="%m%d%Y)`。

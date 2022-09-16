## datetime64

numpy.datetime64是以64位的数据来保存日期，其中包含Y, M, W, D, h, m, s, ms, us。一些常见的日期运算包括：
- np.datetime64('2000-11-27') + 2：按天相加的结果为2000-11-29，numpy自动识别日期类型
- np.datetime64('2000-11') + 2：按天相加的结果为2001-01，numpy自动识别日期类型
- some_date + np.timedelta64(4, 'M') + np.timedelta64(3, 'D')：使用timedelta64对象

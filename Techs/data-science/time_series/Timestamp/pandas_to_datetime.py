import datetime
import pandas as pd
import numpy as np

# 1. 字符串格式"1/1/2018", "2018-01-01"
dt = pd.to_datetime('1/1/2018')
print("convert '1/1/2018'")
print(dt) # 2018-01-01 00:00:00
print(type(dt)) # pandas._libs.tslibs.timestamps.Timestamp

print("convert 'Jul 31, 2009'")
dt = pd.to_datetime('Jul 31, 2009')
print(dt) # 2009-07-31 00:00:00
print(type(dt)) # pandas._libs.tslibs.timestamps.Timestamp

# 2. numpy.datetime64 类型
print("convert np.datetime64('2018-01-01')")
dt = pd.to_datetime(np.datetime64('2018-01-01'))
print(dt) # 2018-01-01 00:00:00
print(type(dt)) # pandas._libs.tslibs.timestamps.Timestamp


# 3. datetime.datetime 类型
print("convert datetime.datetime(2018, 1, 1)")
dt = pd.to_datetime(datetime.datetime(2018, 1, 1))
print(dt) # 2018-01-01 00:00:00
print(type(dt)) # pandas._libs.tslibs.timestamps.Timestamp

# 批量转换
print("convert multiply types of time")
dt_series = pd.to_datetime(['1/1/2018', np.datetime64('2018-01-01'), datetime.datetime(2018, 1, 1)])
# 输出：DatetimeIndex(['2018-01-01', '2018-01-01', '2018-01-01'], dtype='datetime64[ns]', freq=None)
print(dt_series)

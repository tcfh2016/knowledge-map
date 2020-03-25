import pandas as pd
import numpy as np
import datetime

time_stamp = pd.Timestamp(datetime.datetime(2012, 5, 1))
print(time_stamp)
# 2012-05-01 00:00:00

time_stamp = pd.Timestamp('2008-05-01')
print(type(time_stamp))
print(time_stamp)
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>
# 2008-05-01 00:00:00

dates = [pd.Timestamp('2012-05-01'),
         pd.Timestamp('2012-05-02'),
         pd.Timestamp('2012-05-03')]
print("dates=%s" %dates)
ts = pd.Series(np.random.randn(3), index=dates)
print(ts)
#2012-05-01   -1.863204
#2012-05-02    1.337686
#2012-05-03    0.173678

start = datetime.datetime(2011, 1, 1)
end = datetime.datetime(2012, 1, 1)

calendar_index = pd.date_range(start, end)
print(len(calendar_index))

business_index = pd.bdate_range(start, end)
print(len(business_index))

# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
pd.date_range(start, periods=1000, freq='M')   # month end frequency
pd.date_range(start, periods=1000, freq='MS')  # month start frequency
pd.bdate_range(start, periods=250, freq='BQS') # business quarter end frequency
pd.date_range(start, end, freq='BM') # business month end
pd.date_range(start, end, freq='W')  # weekly frequency

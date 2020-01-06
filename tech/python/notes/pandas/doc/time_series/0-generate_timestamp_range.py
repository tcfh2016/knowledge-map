import pandas as pd
import datetime

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

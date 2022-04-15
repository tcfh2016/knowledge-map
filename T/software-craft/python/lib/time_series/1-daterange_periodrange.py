import pandas as pd

period_range = pd.Series(pd.period_range('1/1/2011', freq='M', periods=3))
print(period_range)
#0    2011-01
#1    2011-02
#2    2011-03
#dtype: period[M]

period_range = pd.Series(pd.period_range('1/1/2011', freq='D', periods=3))
print(period_range)
#0    2011-01-01
#1    2011-01-02
#2    2011-01-03
#dtype: period[D]

date_range = pd.Series(pd.date_range('1/1/2011', freq='M', periods=3))
print(date_range)
#0   2011-01-31
#1   2011-02-28
#2   2011-03-31
#dtype: datetime64[ns]

date_range = pd.Series(pd.date_range('1/1/2011', freq='D', periods=3))
print(date_range)
dtype: datetime64[ns]
#0   2011-01-01
#1   2011-01-02
#2   2011-01-03
#dtype: datetime64[ns]

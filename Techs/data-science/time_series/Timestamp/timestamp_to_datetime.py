import pandas as pd

ts = pd.Timestamp('15-Sep-2022 08:14:57')
print(type(ts)) # <class 'pandas._libs.tslibs.timestamps.Timestamp'>

date = ts.date()
print(date) # 2022-09-15
print(type(date)) # <class 'datetime.date'>

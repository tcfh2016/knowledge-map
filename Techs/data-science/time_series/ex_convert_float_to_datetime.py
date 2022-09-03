import pandas as pd
import datetime as dt

f = 20180702210001.0

fmt = '%Y%m%d%H%M%S.%f'
time_tuple = dt.datetime.strptime(str(f), fmt)
print(type(time_tuple))
print(time_tuple)
print(time_tuple.date())

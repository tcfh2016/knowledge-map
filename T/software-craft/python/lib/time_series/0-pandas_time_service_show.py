import pandas as pd
import numpy as np
import datetime

dti = pd.to_datetime(['1/1/2018', '2018-01-01',
                 np.datetime64('2018-01-01'),
                 datetime.datetime(2018,1,1)])

print(np.datetime64('2000-11-27') + 2)
print(np.datetime64('2000-11') + 2)
print('datetime.datetime.today() = %s' % (datetime.datetime.today()))
print('type of datetime.datetime.today() = %s' % (type(datetime.datetime.today())))
print('datetime.date.today() = %s' %datetime.date.today())
print('type of datetime.date.today() = %s'% (type(datetime.date.today())))

print(dti)
print(type(np.datetime64('2018-01-01')))
print(type(datetime.datetime(2018, 1, 1)))

time_range = pd.date_range('2018-01-01', periods=3, freq='H')
print(time_range)

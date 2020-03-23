import pandas as pd
import numpy as np
import datetime

dti = pd.to_datetime(['1/1/2018', '2018-01-01',
                 np.datetime64('2018-01-01'),
                 datetime.datetime(2018,1,1)])
print(dti)
print(type(np.datetime64('2018-01-01')))
print(type(datetime.datetime(2018, 1, 1)))

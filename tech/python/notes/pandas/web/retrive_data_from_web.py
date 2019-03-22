import pandas_datareader.data as web
from datetime import datetime
#import urllib.request as request

start = datetime(2016, 9, 1)
end = datetime(2018, 9, 1)

f = web.DataReader('GDP', 'fred', start, end)
f.ix['2018-01-01']

import pandas_datareader.data as web
from datetime import datetime

start = datetime(2016, 9, 1)
end = datetime(2018, 9, 1)

f = web.DataReader('F', 'iex', start, end)
f.info()

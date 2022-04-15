import datetime as dt

f = 20180702210001.0

fmt = '%Y%m%d%H%M%S.%f'
time_tuple = dt.datetime.strptime(str(f), fmt)
print(time_tuple)

#date = dt.datetime.today().date()
date = dt.date(2008, 2, 8)
print(date)

fmt = '%Y%m%d'
print(date.strftime(fmt))
time =  dt.datetime.today().time()
print(time)

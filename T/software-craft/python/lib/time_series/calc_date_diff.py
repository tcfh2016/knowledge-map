import datetime

date = datetime.date(2020, 1, 1)
print(date)
today = datetime.date.today()
print(today)

diff =  today - date

print(type(diff.days))

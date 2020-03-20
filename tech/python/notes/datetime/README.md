year = int(date_split_list[0])
month = int(date_split_list[1])
day = int(date_split_list[2])

now = datetime(year, month, day)
if (now.isoweekday() < 6):


## 如何获得今天的日期 ？

datetime.date.today()  

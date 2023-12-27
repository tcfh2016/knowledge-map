## 读csv


```
import csv

data = []

with open('data.csv') as fp:
    r = csv.reader(fp)
    for row in r:
        data.append([row[0], int(row[1]), float(row[2])])
```



## 写csv

```
data = [('one', 1, 1.5), ('two', 2, 8.0)]
with open('out.csv', 'w') as fp:
    w = csv.writer(fp)
    w.writerows(data)
```

- [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

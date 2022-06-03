## Chapter 7. Input/Output Operations

I/O 通常是大量数据运算时的性能瓶颈。好在当前大部分的数据处理都在100G以下，金融领域数据也
不过几个G的级别，这是Python及其计算相关库可以承担下来的，对于千万亿级别的数据处理则是新
兴技术Hadoop/Mapduce的用武之地。

### Basic I/O with Python

Python本身提供了侧重性能和扩展性的IO能力。

#### 1.Writing Objects to Disk

在将Python对象写入磁盘的时候通常会使用`pickle`来将处理对象的序列化。序列化表示将对象转
换为字节流，而反序列化则是其逆过程。

```
import numpy as np
import pickle
from random import gauss

a = [gauss(1.5, 2) for i in range(1000000)]

pkl_file = open('data.pkl', 'wb')
pickle.dump(a, pkl_file)
pkl_file.close()

pkl_file = open('data.pkl', 'rb')
file_content = pickle.load(pkl_file)
print(file_content[:5])
pkl_file.close()
```

#### 2.Reading and Writing Text Files

Python对于文本文件的处理是它本身所具有的一大优势。

```
import pandas as pd

rows = 5000
a = np.random.standard_normal((rows, 5))
a.round(4)

t = pd.date_range(start='2014/1/1', periods=rows, freq='H')
csv_file = open(path + 'data.csv', 'w')

header = 'date,no1,no2,no3,no4,no5\n'
csv_file.write(header)

for t_, (no1, no2, no3, no4, no5) in zip(t, a):
    s = '%s,%f,%f,%f,%f,%f\n' % (t_, no1, no2, no3, no4, no5)
    csv_file.write(s)

csv_file.close()


csv_file = open(path + 'data.csv', 'r')
for i in range(5):
  print csv_file.readline(),

csv_file = open(path + 'data.csv', 'r')         
content = csv_file.readlines()         
for line in content[:5]:
  print line,
csv_file.close()          

```

#### 3.SQL DATABASE

Python能够与SQL/NonSQL数据库进行对接，而随着Python发布的SQLite3能够很好地用来进行SQL
测试。

```
import sqlite3 as sq3

query = 'CREATE TABLE numbs (Date date, No1 real, No2 real)'
con = sq3.connect(path + 'numbs.db')
con.execute(query)
con.commit()

con.execute('INSERT INTO numbs VALUES(?, ?, ?)', (dt.datetime.now(), 0.12, 7.3))
data = np.random.standard_normal((10000, 2)).round(5)
for row in data:
  con.execute('INSERT INTO numbs VALUES(?, ?, ?)', (dt.datetime.now(), row[0], row[1]))
  con.commit()

pointer = con.execute('SELECT * FROM numbs')
for i in range(3):
  print pointer.fetchone()
```

#### 4.Writing and Reading NumPy Arrays

通常情况下，使用NumPy, Pickle, PyTables来进行数据的存储和检索会比SQL数据库更高效。

### I/O with pandas

pandas可以很方便地用来处理以下数据格式：

- CSV (comma-separated value)
- SQL (Structured Query Language)
- XLS/XSLX (Microsoft Excel files)
- JSON (JavaScript Object Notation)
- HTML (HyperText Markup Language)

### Fast I/O with PyTables

基本上pandas在处理数据的时候是将数据导入内存进行操作，而PyTables支持外存操作。

### Conclusions

SQL 数据库在处理复杂的数据结构，特别是在多个数据表之间存在复杂的关系时，具有特别的优势。
但其效率问题却没有NumPy基于ndarry和Pandas基于DataFrame类型数据处理上表现得好。

在金融及科学领域，通常需要基于array的数据建模方法。这些场景下，使用NumPy, PyTable, pandas
能够带来很好的性能。

企业及研究机构需要确定它所面对的问题，再来选定硬件和软件架构。

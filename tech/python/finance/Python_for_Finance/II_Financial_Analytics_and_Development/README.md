本书的核心内容：展现Python最重要的库、技术、财务分析及应用开发的方法。

## Chapter 4. Data Types and Structures

本章主要讲解有关Python的类型与结构。

### Basic data types

1.int

不会溢出。

2.float

使用float类型的时候通常`import decimal`来控制浮点的精确。

```
import decimal
from decimal import Decimal

decimal.getcontext().prec = 4

print(Decimal(1)/3)
```         

3.string

Python适合用于处理任何大小任何类型的文本文件，用来表示文本的数据类型便是string。

string包含了许多方法，并且Python支持字符串操作的强大工具正则表达式（由`re`模块提供），
在解析字符串的时候使用正则无论在便捷性还是性能上都更胜一筹。

对于时间的处理示例：

```
import re
from datetime import datetime

series = """
         '01/18/2014 13:00:00', 100, '1st';
         '01/18/2014 13:30:00', 110, '2nd';
         '01/18/2014 14:00:00', 120, '3rd'
         """
dt = re.compile("'[0-9/:\s]+'")
result = dt.findall(series)

pydt = datetime.strptime(result[0].replace("'", ""),'%m/%d/%Y %H:%M:%S')
pydt
```

4.基本数据结构

数据结构是那些囊括了多个对象的数据类型。Python提供了几个内建的数据类型：

- tuple：包含任意类型的集合，仅提供少量方法。
- list：包含任意类型的集合，提供较多方法。
- dict：键-值存储对象。
- set：无序且唯一的对象集合。


### Basic data structures

### NumPy data structures

### Vectorization of code

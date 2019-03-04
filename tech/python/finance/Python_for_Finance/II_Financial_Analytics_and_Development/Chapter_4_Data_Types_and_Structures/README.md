
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

### Basic data structures

数据结构是那些囊括了多个对象的数据类型。Python提供了几个内建的数据类型：

1.tuple

tuple：包含任意类型的集合，仅提供少量方法。

2.list

list可以包含任意类型的集合，提供较多方法。

在Python里尽可能少地使用循环，尽可能使用列表解析，map/filter/reduce函数，以及lambda。

3.dict

键-值存储对象。

4.set

序且唯一的对象集合。


### NumPy data structures

NumPy是专门为科学、财务领域提供的更加便捷和高效地操作数据的函数库，这些数据通常被组织成
数组（array）的形式。

比如我们可以使用list简单的组织多维数组，并能够很好的选择某行或者某个元素，但无法选择某列
的数据。

1.REGULAR NUMBERPY ARRAYS

numpy.ndarray用来专门处理n维数组，它有多个内建方法，以及实现向量化数据操作。

```
import numpy as np
a = np.array([0, 0.5, 1.0, 1.5, 2.0])

a.sum()
a.std()
a.cumsum()

a ** 2     # 每个元素进行平方
np.sqrt(a) # 每个元素进行开方
```

不管是单维还是多维都能够统一操作所有元素，并且能够很好访问单行、单列或者单个数据的数据。

numpy.ndarray 对象的初始化方法有两种：

- 通过已知列表来初始化；
- 另一种方式是在程序执行时自动生成数据来初始化。

2.STRUCTURED ARRAYS

NumPy提供的结构化数组支持不同列使用不同的数据类型：

```
dt = np.dtype([('Name', 'S10'), ('Age', 'i4'),                    
               ('Height', 'f'), ('Children/Pets', 'i4', 2)])        
s = np.array([('Smith', 45, 1.83, (0, 1)),                       
              ('Jones', 53, 1.72, (2, 2))], dtype=dt)
```

如果的dtype规定了每列的数据类型。

### Vectorization of code

代码的向量化是让代码更为简洁并且能够尽可能执行得更快，它的基本思路是让一个比较复杂的对象
一次性执行某项函数，而不用遍历对象里面的每个元素。比如函数编程工具map, filter, reduce就
提供了向量化处理，而NumPy实现上也有向量化的处理。

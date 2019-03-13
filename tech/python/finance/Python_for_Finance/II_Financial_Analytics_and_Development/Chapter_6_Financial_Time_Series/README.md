## Chapter 6. Financial Time Series

金融领域最主要的数据之一是时间序列，Python里的pandas库，由Wes McKinney开发。本章主要介
绍pandas的基本使用方法、如何处理web, csv数据,以及高频次数据。

### pandas Basics

pandas是基于NumPy，因此NumPy的很多通用函数都可以应用在pandas对象上。

1.First Steps with DataFrame Class

DataFrame 用来管理基于索引和标签的数据，它与SQL数据表和电子表格稍有区别。

```
import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
print(df)            
```

如上代码对应如下输出：

```
λ python pandas_basic_use.py
   numbers
a       10
b       20
c       30
d       40
```

DataFrame按照Data, Labels和Index的方式来组织数据：

- Data，可以使用不同的类型，除了内建类型外，还支持list, tuple, ndarray, and dict。
- Labels，Data按照列进行组织，Label是不同列的标签。
- Index，用于索引每列的数据，可以支持numbers, strings, time几种类型。

相比ndarray，DataFrame在扩充已有对象时能够更便捷。

2.

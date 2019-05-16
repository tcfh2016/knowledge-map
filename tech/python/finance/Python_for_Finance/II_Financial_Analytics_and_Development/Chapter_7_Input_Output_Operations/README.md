## Chapter 6. Input/Output Operations

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

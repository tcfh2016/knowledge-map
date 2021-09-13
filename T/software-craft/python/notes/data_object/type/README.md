## 数字

包括整数、浮点数、二进制、分数等，支持加法和乘法等操作。

整数，包括 `+ - * / ** % //`六种算术运算。Python对整数的长度没有限制。浮点，所有适用整
数的算术运算均适合浮点类型，然而浮点数存在上限和下限，且可能产生溢出。基于这一点考虑通常
优先考虑整数。decimal模块可用于控制浮点数的操作。

Python携带的`math`函数库提供了常用的数据处理函数。

Python提供了很多内置函数来进行类型转换：

- 将整数转换为浮点数，比如`float(3)`。
- 将字符串转换为浮点数，比如`float('3.0')`。
- 使用`str(87)`将数字转换为字符串。
- 自动类型转换，比如整数与浮点类型的运算结果自动转换为浮点类型。
- 将浮点型转换为整形可以使用 `int(8.64)`也可以使用`round(8.64)`，前者直接将小数部分删
  除，后者的策略比较特殊，即圆整到最接近的偶数。
- 内置函数`hex(I)`、`oct(I)`和`bin(I)`把一个整数转换为对应进制的字符串。
- 内置函数`int(str, base)`根据指定的进制把字符串转换为一个整数。


## bytes

`bytes`类提供了不可变的序列，里面的值必须是介于0~255的整书。但`bytearray`提供了一个可变的序列。常见方法：

- bytes_array.count(byte)
- bytes_array.index(byte)
- bytes_array.append(byte)
- bytes_array.remove(byte)
- bytes_array.insert(index, byte)
- bytes_array.pop(byte)

## string

- len(str)
- min(str)
- max(str)
- str.count(ch)
- str.find(ch)
- str.startswith(sub_str)
- str.endswith(sub_str)
- str.upper()
- str.lower()
- str.split(ch)

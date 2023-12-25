## 数字

包括整数、浮点数、二进制、分数等，支持加法和乘法等操作。

整数，包括 `+ - * / ** % //`六种算术运算。Python对整数的长度没有限制。浮点，所有适用整数的算术运算均适合浮点类型，然而浮点数存在上限和下限，且可能产生溢出。基于这一点考虑通常优先考虑整数。decimal模块可用于控制浮点数的操作。

Python携带的`math`函数库提供了常用的数据处理函数。同时还有很多内置函数来进行类型转换：

- 将整数转换为浮点数，比如`float(3)`。
- 将字符串转换为浮点数，比如`float('3.0')`。
- 使用`str(87)`将数字转换为字符串。
- 自动类型转换，比如整数与浮点类型的运算结果自动转换为浮点类型。
- 将浮点型转换为整形可以使用 `int(8.64)`也可以使用`round(8.64)`，前者直接将小数部分删除，后者的策略比较特殊，即圆整到最接近的偶数。
- 内置函数`hex(I)`、`oct(I)`和`bin(I)`把一个整数转换为对应进制的字符串。
- 内置函数`int(str, base)`根据指定的进制把字符串转换为一个整数。


## 表示法

- `1e-6`：科学计数法
- `0xFF`：16进制
- `0b101010`：2进制

## 浮点数

浮点数（float类型）可以用指数形式来表示，1.23e3表示1.23乘以10的3次方。

问题：如何保留小数点后2位？

`round()`函数我初以为是用来预留2位小数点的，但实际上并不是这么简单，比如`1707.643`和`347.397`分别使用`round(x, 2)`前者的输出为`1707.64`，后者的输出为`347.4`，并不是保留了2位小数。

这个函数的用意并不简单是“保留n位小数点”，而是将一个“十进制的小数”圆整（四舍五入）到最接近的“浮点数”，所以：

- `round(2.755, 2)`的值不为常见四舍五入的“2.76”，而是“2.75”。
- `round(2.395, 2)`的值为“2.40”，而是“2.4”（没有保留小数点后2位）。

其实保留小数点后2位算是一个格式化输出的问题，可以使用`{:.2f}`:

```
print("f1 = {:.2f}, f2 = {:.2f}".format(round(f1,2), round(f2,2)))
```

参考：

- [How to display two decimal points in python, when a number is perfectly divisible?](https://codeberryschool.com/blog/en/python-round/)
- [How to use the Python Round method – with examples](https://stackoverflow.com/questions/70882733/how-to-display-two-decimal-points-in-python-when-a-number-is-perfectly-divisibl)
- [round](https://python-reference.readthedocs.io/en/latest/docs/functions/round.html)

## 整数除法

使用`//`来进行整数除法，返回比结果小的最大整数。

```
11/4 = 2.75
11//4 = 2
```

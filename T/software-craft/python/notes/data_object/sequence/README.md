## 序列

包括字符串、列表、元组，支持索引、分片和合并等操作。

序列的索引是按照从最前面的偏移量进行编码的，也就是从0开始，第一项索引为0，第二项索引为1，依次类推。Python支持反向索引，从最后一个开始计算。一般来说，负的索引号会简单地与字符串的长度相加。

需要留意的是，尽管序列操作是通用的，但方法不通用。一条简明的法则是这样的：可作用于多种类型的通用型操作都是以内置函数或表达式的形式出现的（比如len(X), x[0]），但类型特定的操作是以方法调用的形式出现的（比如string.upper()）。你可以通过dir来查看对象支持的所有方法，并使用help来查找帮助信息。


## 切片

无论是可变序列（list, bytearray）还是不可变序列（tuple, string, bytes）都支持切片操作。

首先对于这些序列的元素都能够按照索引进行访问，索引从前往后从0开始，从后往前自-1开始，以list为例：

```
[a, b, c, d, e, f, g]
 0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2 -1
```

序列的切片遵循前闭后开的原则：[start, end)，同时也支持省略：省略start默认从第一个元素开始，省略end，默认最后一个元素+1。三种切片形式：

```
list[0:2]
list[0:]
list[:2]
list[0:2:1] 指定切片间隔/步长
```

## 常见问题

1. 如何查找列表中某个元素的下标？

参考：

- [Finding the index of an item in a list](https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list)
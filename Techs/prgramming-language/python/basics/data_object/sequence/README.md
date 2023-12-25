## 序列

序列包括字符串、列表、元组，支持索引、分片和合并等操作。

需要留意的是，尽管序列操作是通用的，但方法不通用。一条简明的法则是这样的：可作用于多种类型的通用型操作都是以内置函数或表达式的形式出现的（比如len(X), x[0]），但类型特定的操作是以方法调用的形式出现的（比如string.upper()）。你可以通过dir来查看对象支持的所有方法，并使用help来查找帮助信息。


## bytes

`bytes`类提供了不可变的序列，里面的值必须是介于0~255的整书。但`bytearray`提供了一个可变的序列。常见方法：

- bytes_array.count(byte)
- bytes_array.index(byte)
- bytes_array.append(byte)
- bytes_array.remove(byte)
- bytes_array.insert(index, byte)
- bytes_array.pop(byte)

## 索引

序列的索引是按照从最前面的偏移量进行编码的，也就是从0开始，第一项索引为0，第二项索引为1，依次类推。

Python支持反向索引（负的索引），从最后一个开始计算。`-1`引用最后一个元素，`-2`引用倒数第二个元素。


## 切片

无论是可变序列（list, bytearray）还是不可变序列（tuple, string, bytes）都支持切片操作。所谓“切片”，就是通过指定索引范围对元素进行引用的方法。

首先对于这些序列的元素都能够按照索引进行访问，索引从前往后从0开始，从后往前自-1开始，以list为例：

```
[a, b, c, d, e, f, g]
 0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2 -1
```

注意：使用切片时，最后一个作为终点的元素是不包含在范围内的。也就是遵循前闭后开的原则：[start, end)，同时也支持省略：省略start默认从第一个元素开始，省略end，默认最后一个元素+1。三种切片形式：

```
list[0:2]
list[0:]
list[:2]
list[0:2:1] 指定切片间隔/步长
```


## 如何查找列表中某个元素的下标？

```
["foo", "bar", "baz"].index("bar")
```

如果查找不到会抛出异常，所以这里需要使用`elem in list`或者使用`try/execept`来捕获异常。

参考：

- [Finding the index of an item in a list](https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list)

## 如何根据条件查找 ？


```
next(x for x in the_iterable if x > 3) # 找不到返回StopIteration 
next((x for x in the_iterable if x > 3), default_value) # 找不到返回default_value
```

参考：

- [Get the first item from an iterable that matches a condition](https://stackoverflow.com/questions/2361426/get-the-first-item-from-an-iterable-that-matches-a-condition)

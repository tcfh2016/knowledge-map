Python自带了很多内置函数以及函数库，并且你能够很方便的获取帮助。

- 使用`dir(module_name)`列出模块的所有函数。
- 使用`dir(__builtins__)`查看内置函数清单。
- 使用`help(function_name)`查看出该函数的文档字符串。
- 使用`print(module_name.function_name.__doc__)`打印出该函数的文档字符串。

Python里的赋值语句`x = expr`与其他语言里的含义不一样，比如在C/C++里是先为`x`分配内存，再将`expr`的值拷贝到`x`的内存。但是在Python里则表示是将 `x`指向`expr`，即先为`expr`的值分配空间，再将`x`指向它。所以，Python里的赋值操作不会进行值拷贝，而仅仅改变变量所指向的位置。Python自动跟踪所有的值，对于没有任何变量指向的值则将其删除，此即为`垃圾收集`。

理解了如上的概念，便能理解`x = None`的含义是将`x`重置为初始状态。

参考

- [The Python Standard Library](https://docs.python.org/2.7/library/index.html)
- [What is a None value?](https://stackoverflow.com/questions/19473185/what-is-a-none-value#)

# 内置函数

## `isinstance()`

使用格式为`isinstance(object, type)`，其中object是某个特定的对象，而type则是一个或者
多个内建类型或者类。当type为包含多个类型的元组时，只要object属于元组中的某种类型即返回
True。

## `round(x, [, n])`

返回浮点数的四舍五入值，n可以指定小数点后面的位数。


## `dir()`
模块文件里通常包含多个变量名，内置的dir函数可以获得模块内部的可用的变量名列表。

## `zip()`

zip()根据传入的数据返回一系列可以迭代的元组。比如，如下代码将两个列表组合成多个元组，通常用来构造字典数据（`d = dict(zip(keys, values))`）：

```
keys = range(1, 5)
values = range(10, 41, 10)

tuple_list = zip(keys, values)
print(tuple_list)
print([pair for pair in tuple_list])
# 输出 [(1, 10), (2, 20), (3, 30), (4, 40)]
```

同时通过`*zip`可以进行unzip/unpack的操作，比如：

```
unzip_list = zip(*zip(keys, values))
print(unzip_list)
print([pair for pair in unzip_list])

# 输出 [(1, 2, 3, 4), (10, 20, 30, 40)]
```

参考：

- [Python zip()](https://www.programiz.com/python-programming/methods/built-in/zip)

## `type()`

显示对应数据的类型。

## `eval()`

内置函数`eval`能够把字符串当作可执行程序代码，可以将字符串转换成对象。但它过于强大，会简
单地执行Python的任何表达式。如果想存储Python的原生对象，但又无法信赖文件的数据来源，Python
的标准库pickle模块会是个理想的选择。

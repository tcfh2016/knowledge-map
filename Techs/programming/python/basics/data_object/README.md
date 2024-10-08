## 基本数据类型

Python里的任何类型都被视作object，可以使用 `type(t)`命令来查看值或者变量的数据类型。

Python内置类型可以分为数字、序列、和映射三大类，但实际上包括了数字、字符串、列表、字典、元组、文件、集合、用户定义类型及其他比如布尔型、None等。四种常见的变量类型为`int`, `float`, `str`, `bool`。`bool`型可以看成特殊的二值变量，取值为`True`和`False`。

- [数字](./number/README.md)
- [序列](./sequence/README.md)
- [集合](./set/README.md)
- [映射](./dict/README.md)

其中的列表和字典是可变的，而数字、字符串、元组是不可变的。

## 动态类型

Python中类型是在运行过程中自动决定的，而不是通过代码声明。Python中的变量是一个系统表的元素，永远不会有任何和它关联的类型信息或约束，类型的概念存在于对象中而不是变量名中，变量仅拥有指向对象连接的空间。对象是分配的一块内存，有足够的空间去表示它们所代表的值。每个对象都有两个标准的头部信息：一个类型标志符去标识这个对象的类型，以及一个引用的计数器，用来决定是不是可以回收这个对象。

当变量出现在表达式中时，它会马上被当前引用的对象所代替。

## 类型转换

类似的转换函数包括`str()`, `int()`, `float()`, `bool()`。


###  ValueError: invalid literal for int() with base 10: '1.0'

如果将`1.0`通过`int('1.0')`的方式来转换会报错，需要使用`int(float('1.0'))`的方式来转换。

## 变量

其他变成语言中使用变量时需要提前进行声明，但是在Python中不需要，仅仅只需给变量代入值即可。在数据类型上，因为Python是采用“动态类型”，所以也是在变量被赋值的时候才确定，并且变量会随着所附值不同而改变其类型。

Python里面支持可以同时为多个变量赋值的操作：

```
x, y = 4, 2
```

变量的名称第一个字符必须是字符串或下划线，不能是数字。

## 相等性

"=="操作符测试值的相等性，递归地比较所有内嵌对象。"is"表达式测试对象的一致性，测试二者是否是同一个对象。


## 引用 vs 拷贝

赋值操作总是储存对象的引用，而不是拷贝，所以赋值操作会产生相同对象的多个引用，如果在原处修改可变对象可能会影响程序中其他地方对相同对象的其他引用。

如果需要拷贝，需要明确要求，下面四种方式均能创建拷贝：

- 没有限制条件的分片表达式(L[:])能够复制序列。
- 字典copy方法（X.copy()）能够复制字典。
- 有些内置函数（例如,list）能够生成拷贝。
- copy标准库模块能够生成完整拷贝。

无条件值的分片以及字典copy方法只能做顶层复制，不能够复制嵌套的数据结构。如果你需要一个深层嵌套的数据结构的完整的、完全独立的拷贝，那么就要使用标准的copy模块。


## 默认值的问题

一个变量在还没有确定其类型的时候，初始值应该填写为什么？

最常见的是使用`None`，有时使用`object()`。None是一种特殊的数据类型，起空的占位符的作用，与C语言中的NULL指针类似。

参考：

- [Initialize parameter of method with default value](https://stackoverflow.com/questions/13075044/initialize-parameter-of-method-with-default-value)
- [Default Parameter Values in Python](http://effbot.org/zone/default-values.htm)


## 判断类型

```
# 判断o的类型是不是str或者str的子类
if isinstance(o, str):

# 判断o的类型是不是str
if type(o) is str:
if type(o) == str:    
```

参考：

- [What's the canonical way to check for type in Python?](https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python)
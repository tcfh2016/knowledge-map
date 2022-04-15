# 基本数据类型

Python里的任何类型都被视作object，可以使用 `type(t)`命令来查看值或者变量的数据类型。Python主要的内置类型可以分为数字、序列、和映射三大类，但实际上包括了数字、字符串、列表、字典、元组、文件、集合、用户定义类型及其他比如布尔型、None等。

- [数据类型](./type/README.md)
- [作用域](./scope/README.md)
- [文件](./file/README.md)
- [序列](./sequence/README.md)
- [集合](./set/README.md)
- [映射](./map/README.md)
- [自定义类型](./user-defined-type/README.md)

# 常见问题

## 多项赋值

Python里面支持可以同时为多个变量赋值的操作：

```
x, y = 4, 2
```

## 动态类型

Python中类型是在运行过程中自动决定的，而不是通过代码声明。Python中的变量是一个系统表的元素，永远不会有任何和它关联的类型信息或约束，类型的概念存在于对象中而不是变量名中，变量仅拥有指向对象连接的空间。对象是分配的一块内存，有足够的空间去表示它们所代表的值。每个对象都有两个标准的头部信息：一个类型标志符去标识这个对象的类型，以及一个引用的计数器，用来决定是不是可以回收这个对象。

当变量出现在表达式中时，它会马上被当前引用的对象所代替。------

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


## 有关不同对象类型的作用域疑问

如下的代码为打印 “UnboundLocalError: local variable 'flag' referenced before assignment” 的错误，其原因在于对象flag没有声明为全局变量。然而，其疑问点在于为什么对象list没有问题，但是对象flag有问题呢？

```
list = [1, 2, 3, 4, 5]
flag = False

def test_scope():
    for i in list:
        print(i)
        if (not flag):
            flag = True

test_scope()
```

这里的关键点在于紧随`if (not flag)`之后的`flag = True`语句，由于Python会在对象被赋值的时候重新定义对象的作用域，因此Python在编译的时候由于看到`flag = True`会将flag视为本地变量，这恰好与位于赋值语句之前的`if (not flag)`相冲突。

*190603 注：其实这里的 not flag和 flag = True 前后两条语句对于 flag绑定在一起的原因在于相同函数里的局部变量同属相同作用域，因此不可能 not flag 引用的是global 变量，而flag = True 引用的是局部变量。由于 flag 被赋值因此被转换为局部变量，这导致 not flag在引用时并未赋值。*

总结几点:

- 在模块顶层定义的对象具有全局作用域，模块均可以访问它。
- 函数内部的赋值语句创建了本地变量，它与同名的全局变量是不同的并且会隐藏它。
- 不允许修改嵌套的def作用域中的名称。
- 在一个函数内部却位于模块文件顶层的变量名赋值，会涉及到作用域改变的问题，因此如果需要给该全局变量赋值，那么需要在函数内部通过global语句生明。

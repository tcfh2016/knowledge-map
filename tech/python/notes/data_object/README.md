# 内容索引

- [数据类型](./type/README.md)
- [作用域](./scope/README.md)

# 常见问题

1.有关不同对象类型的作用域疑问

如下的代码为打印 “UnboundLocalError: local variable 'flag' referenced before assignment” 的错误，其原因在于对象flag没有声明为全局变量。然而，其疑问点在于为什么对象
list没有问题，但是对象flag有问题呢？

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

这里的关键点在于紧随`if (not flag)`之后的`flag = True`语句，由于Python会在对象被赋值
的时候重新定义对象的作用域，因此Python在编译的时候由于看到`flag = True`会将flag视为本
地变量，这恰好与位于赋值语句之前的`if (not flag)`相冲突。

*190603 注：其实这里的 not flag和 flag = True 前后两条语句对于 flag绑定在一起的原因
在于相同函数里的局部变量同属相同作用域，因此不可能 not flag 引用的是global 变量，而
flag = True 引用的是局部变量。由于 flag 被赋值因此被转换为局部变量，这导致 not flag在
引用时并未赋值。*

总结几点:

- 在模块顶层定义的对象具有全局作用域，模块均可以访问它。
- 函数内部的赋值语句创建了本地变量，它与同名的全局变量是不同的并且会隐藏它。
- 不允许修改嵌套的def作用域中的名称。
- 在一个函数内部却位于模块文件顶层的变量名赋值，会涉及到作用域改变的问题，因此如果需要给
该全局变量赋值，那么需要在函数内部通过global语句生明。
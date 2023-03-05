Python创建、改变或查找变量名都是在所谓的命名空间（一个保存变量名的地方）中进行的，一个变量在被赋值的地点被绑定给特定的命名空间。因此，Python中变量被赋值的地方决定了它的命名空间，也即是它的可见范围，或者说作用域。


## 作用域法则

- 函数定义了本地作用域，模块定义了全局作用域。
- 全局作用域的作用范围仅限于单个文件。
- 赋值的变量名除非声明为全局变量或非全局变量，否则均为本地变量。
  - 如果要给一个函数内部却位于模块文件顶层的变量名赋值，需要在函数内部通过global语句生明。
  - 如果需要给一个嵌套的def中的名称赋值，从Python3.0开始可以通过nonlocal语句生明。

*注：原处改变对象并不会把变量划分为本地变量，只有对变量名赋值才可以。*  


## 变量名解析规则：LEGB规则

当引用一个变量时，Python按如下顺序查找：从本地变量中，在任意上层函数的作用域，在全局作用域，最后在内置作用域中查找。变量在代码中被赋值的位置通常决定了它的作用域。

- L，本地作用域
- E，上一层结构中def或lambda的本地作用域
- G，全局作用域
- B，内置作用域

如上的L作用域通常是在函数体内的局部作用域，而E作用域则常出现在函数嵌套的过程中。


## global语句与nonlocal语句

global使得作用域查找从嵌套的模块的作用域开始，并且允许对那里的名称赋值。但是，对全局名称的赋值总是在模块的作用域中创建或修改他们。

nonlocal限制作用域查找只是嵌套的def，要求名称已经存在于那里，并且允许对它们赋值。作用域查找不会继续到全局或内置作用域。

比如如下的代码在嵌套的nested()函数中修改status的值会修改其作用域，从而出现
“nboundLocalError: local variable 'status' referenced before assignment”的错误，可以通过添加nonlocal关键字解决。

```
def test_scope(start):
    status = start
    def nested():
        #nonlocal status
        print(status)
        status += 1
    return nested
```


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

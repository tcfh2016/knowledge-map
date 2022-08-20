# 函数定义

函数是一大块可重用的代码。它通过`def`关键字进行定义，并遵从特定的格式。

- 函数可以有0个或者多个参数。
- 函数可以有返回值，也可以无返回值。
- 调用函数必须指定`()`。

# 函数命名

与变量一样，函数名也只能包含字母、数字和下划线，且不能以数字开头。main()函数在python里面不是必需的，但仍旧被认为是程序的起点。

# 变量作用域

函数内定义的变量、参数都是局部变量，它们只在函数内有效。定义在函数外的变量是全局变量，在函数里面访问全局变量需要用`global`关键字进行声明：

```
name = 'jack'
def global_variable():
    global name
    name = 'loucy'
```

使用可以修改的变量，比如string, list。对于其他需要其他方式

参考：

- [How do I pass a variable by reference?](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)

## 函数参数

python里不支持按值传递，所有的参数都是按引用传递。只不过在函数里面对于参数值的更改是不生效的。

默认参数的定义与C中一样。



# [pass语句](https://stackoverflow.com/questions/13886168/how-to-use-the-pass-statement-in-python)

`pass`语句实际上是一个空语句，通常用来占位，比如当你定义了一些函数但是还不想着立即实现它
们。

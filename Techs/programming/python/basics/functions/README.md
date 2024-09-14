## 函数定义

函数是一大块可重用的代码。它通过`def`关键字进行定义，并遵从特定的格式。

- 函数可以有0个或者多个参数。
- 函数可以有返回值，也可以无返回值。
- 调用函数必须指定`()`。


## 函数命名

与变量一样，函数名也只能包含字母、数字和下划线，且不能以数字开头。main()函数在python里面不是必需的，但仍旧被认为是程序的起点。


## 变量作用域

函数内定义的变量、参数都是局部变量，它们只在函数内有效。定义在函数外的变量是全局变量，在函数里面访问全局变量需要用`global`关键字进行声明：

```
name = 'jack'
def global_variable():
    global name
    name = 'loucy'
```

使用可以修改的变量，比如string, list（只能修改内部的值）。对于其他就需要定义全局变量的方式。

参考：

- [How do I pass a variable by reference?](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)


## 函数参数

函数参数包括“位置参数”和“关键字参数”两种，两者同时出现时“位置参数”必须写在前面。

“位置参数”的意思就是按照声明的定义来访问，而“关键字参数”是以类似“参数名=值”这样指定参数的形式，使用关键字指定参数值，常在指定函数的默认值时使用。

python里不支持按值传递，所有的参数都是按引用传递。只不过在函数里面对于参数值的更改是不生效的。

默认参数的定义与C中一样。

## 不定长参数

使用`*args`仅仅支持不定长的位置参数，获取到的`args`是一个元组：

```
def add(x, *args):
    total = x
    for arg in args:
        total += arg
    return total
```

使用`**args`可以支持关键字参数，获取到的`args`是一个字典：

```
def add(x, **kargs):
    total = x
    for arg, value in kargs.items():
        total += value
    return total
```

## 返回值

返回值可以没有，也可以有一个或者多个。当返回多个时，多个参数会拼成一个元组返回。

```
def div(a, b):
    value = a // b
    remain = a % b

    return value, remain
```

## 函数中的函数

参考：

- [Python Inner Functions: What Are They Good For?](https://realpython.com/inner-functions-what-are-they-good-for/)


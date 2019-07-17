# 模块

模块是Python里最高级别的程序组织单元，它将程序代码和数据封装起来以便重用。每一个文件都是
一个模块，并且模块导入其他模块之后就可以使用导入模块定义的变量名。在模块导入时，模块文件
的全局作用域变成了模块对象的命名空间（即导入给予了对模块的全局作用域中的变量名的读取权）。

一个Python程序包括了多个含有Python语句的文本文件，程序由一个主体的、顶层文件，配合零个
或多个支持文件。顶层文件（又称为脚本）包含了程序的主要控制流程，模块文件就是工具库，前者
使用后者定义的工具，后者可能还使用其他模块定义的工具。

模块术语的变化：

- 模块文件常常作为Python写成的程序。也就是说，一个程序是由一系列预编写好的语句构成，保存在
文件中，从而可以反复执行。
- 可以直接运行的模块文件往往也叫做脚本（一个顶层程序文件的非正式说法）。
- 有些人将“模块”这个说法应用于被另一个文件所导入的文件。

# 编写模块代码

## 模块的创建

任何以.py为后缀名的Python文件都被自动认为是Python模块。当一个模块被导入时，Python会把内
部模块名映射到外部文件名，也就是通过把模块搜索路径中的目录路径加在前面，而.py或其他后缀名
添加在后边。

## 模块的使用

- `import x`语句：读取整个模块，并用x来代表整个模块对象，具体属性需要通过x.y来引用。
- `from x import y`语句：将变量名复制到另一个作用域，直接通过y引用对应变量。
  - from语句会在导入中创建新变量，这些变量初始化时引用了导入文件中的同名对象；
  - 如上语句相当于先`import x`再`y = x.y`。
- `from x import *`语句：取得x模块顶层所有赋了值的变量名的拷贝。

import和from是可执行的语句，而不是编译期间的声明，它们可以嵌套在if测试、函数def中，直到
执行程序时才会进行解析。

使用`from x import *`导入变量可能破坏命名空间，即其中有变量名与当前作用域中变量同名，因
此通常限制在每个文件中只使用一次，多数from语句用于明确列出想要的变量，而简单的模块倾向于
使用import。

## 模块命名空间

模块就是命名空间，即变量名创建的场所，存在于模块之内的变量名就是模块对象的属性，它们是以
字典的形式储存的，可以通过`list(module.__dict__.keys())`来打印所有属性。

文件导入后需要点号运算符放读取变量名，点号运算可用于任何具有属性的对象：模块、类、C扩展类型等。

## 重载模块

模块程序代码默认只在导入时执行一次，要强制模块代码重新载入并运行，得调用reload内置函数，
这里面的过程如下：

- 在模块第一次导入（通过import或者from语句）时，该模块被加载并执行；
- 之后的导入只会使用已经加载的模块对象，而不会重载或执行文件的代码；
- reload函数会强制已加载的模块代码重新执行。

在重载之前模块一定是已经预先成功导入的。reload是Python的内置函数不是语句，因此在语法上
小有不同：

```
import module
...use module.attributes...

from imp improt reload
reload(module)
...use module.attributes...
```

# 常见问题

## import 模块之后为什么无法直接使用模块中的变量 ？

参考如下代码，会出现 `AttributeError: module 'tkinter' has no attribute 'messagebox'`
的错误。

```
import time, sys
if sys.version < '3':
    import Tkinter
    #import Tkinter.messagebox
else:
    import tkinter
    #import tkinter.messagebox

window = tkinter.Tk()
tkinter.messagebox.showwarning()    
```

为什么`import tkinter`但是无法使用到 tkinter下面的 messagebox属性呢？

1. 第一次错误的认识

在查阅之前的笔记之后，本来以为是因为Python的`import`语句并不同于C里的`#include`，它仅
仅是搜索该模块，并且编译让后将其存储到`sys.modules`的表里供以后使用，所以这里的`import`
实际上并没有将`tkinter`的相关变量引入当前作用域。但这无法解释为什么`window = tkinter.Tk()`
没有报错。

2. 第二次重新的认识

基于如上的疑问，我在StackOverflow上提了一个问题，读了`funie200`的回答之后了解到`tkinter.Tk()`
是`tkinter`的变量，但`tkinter.messagebox`是`tkinter`里面的模块，因此`messagebox`需要
再次import。

之后认真理解了`Aran-Fey`的回答之后，觉得他回答得真的太好了，细致并且更有深度。他的解释如
下：

  - 在 import module的时候，如果import的是文件，那么会执行该文件；如果import的是其他模
  块（目录），那么此时会执行该模块下的 __init__.py 文件。
  - 这里 messagebox 包括在 tkinter 中，因此import tkinter 那么执行的是其中的__init__.py
  文件，由于其中已经讲 class `Tk()`的定义导入进来，因此可以直接使用。

参考：

- [Why do I need to import tkinter.messagebox but don't need to import tkinter.Tk() after importing tkinter?](https://stackoverflow.com/questions/56268474/why-do-i-need-to-import-tkinter-messagebox-but-dont-need-to-import-tkinter-tk/56268994#56268994)


## 如何import上层目录？

比如在tst目录下面的loan_type_compare.py文件引用了上层目录的capital.py和loan.py，那么
该如何编写import语句：

```
C:.
└─Toolbox
    │  capital.py
    │  loan.py
    │  loan_payment.py
    │  __init__.py
    │
    ├─tst
    │  │  loan_type_compare.py
    │  │  __init__.py
```

尝试在tst里面执行loan_type_compare.py文件提示：

```
λ python loan_type_compare.py
Traceback (most recent call last):
  File "loan_type_compare.py", line 3, in <module>
    from .. import capital
ValueError: attempted relative import beyond top-level package
```

这是因为当以tst作为工作目录的时候，Python无法探知当前包的结构，也即是说Python不知道tst
是存在于一个包结构当中，因此无法访问基于包的父目录。你可以在Tool上级目录通过`import Toolbox.tst.loan_type_compare`
来执行，但在Toolbox目录执行`tst.loan_type_compare`，或者在tst目录执行`loan_type_compare`
都会提示相同的错误。

因此，按照模块、包的概念：一般Python程序的组织是以“一个顶层文件+零个或多个支持文件”组成，
这里的测试文件为顶层文件，应该布置在上层目录。

参考：

- 《Python学习手册》第五部分：模块
- [beyond top level package error in relative import](https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import)

# 内容索引

- [模块](./module/README.md)

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

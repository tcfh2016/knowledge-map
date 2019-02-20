
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

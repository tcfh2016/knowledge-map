
## 如何import上层目录？

比如在tst目录下面的loan_type_compare.py文件引用了上层目录的capital.py和loan.py，那么
该如何编写import语句：

```
C:.
│  capital.py
│  loan.py
│
├─tst
│      loan_type_compare.py
```

这里设计到模块、包的概念。一般Python程序的组织是以“一个顶层文件+零个或多个支持文件”组成，
这里的测试文件为顶层文件，应该布置在上层目录。

参考：

- 《Python学习手册》第五部分：模块

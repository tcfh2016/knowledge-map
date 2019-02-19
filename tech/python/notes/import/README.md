
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

这里设计到模块包的概念，

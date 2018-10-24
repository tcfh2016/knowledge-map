
# Debug

编写完一篇源代码，如何开始调试？

第一步：单纯通过编译来进行检查。

```
python -m py_compile script.py
```

第二步：使用调试工具。

- PDB
- logging

# logging

logging相比print打印有不少优势，首先，print语句供临时使用用，在调试的时候添加，调试之后
需要删除。其次，print只能够打印到终端，而logging可以输出到指定的文件。再次，logging还能
够进行日志分级控制。

logging打印的日志分5个层级：

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

今天碰到一个日志的问题，使用单元测试的时候日志模块能够正常的转储日志，但是正常使用命令行
执行程序却没有日志文件，不知道什么原因。

晚上吃饭的时候想到可能是当前的日志是在__init__里面初始化的，然而这种初始化是否和单元测试
本身紧密相关呢？

# pdb

调试代码的时候发现添加打印比较麻烦，查找了一下，发现原来使用pdb非常简单。

- import pdb；
- 添加`pdb.set_trace`作为断点；
- 执行程序，基本用法类似gdb。



# 参考

- [How can I check the syntax of Python script without executing it?](https://stackoverflow.com/questions/4284313/how-can-i-check-the-syntax-of-python-script-without-executing-it/8437597)
- [PythonDebuggingTools](https://wiki.python.org/moin/PythonDebuggingTools)
- [Python Conquers The Universe](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/)

- [Python Logging Tutorial](http://www.patricksoftwareblog.com/python-logging-tutorial/)
- [Python 程序如何高效地调试？](https://www.zhihu.com/question/21572891)

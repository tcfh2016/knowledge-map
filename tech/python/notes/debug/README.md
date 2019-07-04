# 交互模式

交互模式根据用户的输入运行代码并响应结果，是实验和测试的好地方。如下是几个使用交互模式的
技巧：

- 只能够输入Python命令。
- 交互模式不需要输入完整的打印语句，直接键入变量名就可。
- 输入符合语句时交互模式的提示符会从“>>>”变为“...”。
- 输入符合语句时，用一个空行结束符合语句。
- 交互模式一次只运行一条语句（包括单语句或者符合语句），也即不能像在文件里面同时运行多条
语句，比如下面这段代码会打印错误：

```
>>> for x in 'spam':
...     print(x)     # 这是符合语句，需要键入空格来结束并运行。
... print('done')    # 这是另一条语句，必须运行完上条语句后才能运行这条。
  File "<stdin>", line 3
    print('done')
        ^
SyntaxError: invalid syntax
```


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

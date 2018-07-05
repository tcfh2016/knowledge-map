
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

# 参考

- [How can I check the syntax of Python script without executing it?](https://stackoverflow.com/questions/4284313/how-can-i-check-the-syntax-of-python-script-without-executing-it/8437597)
- [PythonDebuggingTools](https://wiki.python.org/moin/PythonDebuggingTools)
- [Python Conquers The Universe](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/)

- [Python Logging Tutorial](http://www.patricksoftwareblog.com/python-logging-tutorial/)

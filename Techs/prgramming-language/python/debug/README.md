## 交互模式

交互模式根据用户的输入运行代码并响应结果，是实验和测试的好地方。如下是几个使用交互模式的技巧：

- 只能够输入Python命令。
- 交互模式不需要输入完整的打印语句，直接键入变量名就可。
- 输入符合语句时交互模式的提示符会从“>>>”变为“...”。
- 输入符合语句时，用一个空行结束符合语句。
- 交互模式一次只运行一条语句（包括单语句或者符合语句），也即不能像在文件里面同时运行多条语句，比如下面这段代码会打印错误：

```
>>> for x in 'spam':
...     print(x)     # 这是符合语句，需要键入空格来结束并运行。
... print('done')    # 这是另一条语句，必须运行完上条语句后才能运行这条。
  File "<stdin>", line 3
    print('done')
        ^
SyntaxError: invalid syntax
```


## Debug

编写完一篇源代码，如何开始调试？第一步：单纯通过编译来进行检查。

```
python -m py_compile script.py
```

第二步：使用调试工具，比如PDB和logging。


## 参考

- [How can I check the syntax of Python script without executing it?](https://stackoverflow.com/questions/4284313/how-can-i-check-the-syntax-of-python-script-without-executing-it/8437597)
- [PythonDebuggingTools](https://wiki.python.org/moin/PythonDebuggingTools)
- [Python Conquers The Universe](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/)
- [Python 程序如何高效地调试？](https://www.zhihu.com/question/21572891)

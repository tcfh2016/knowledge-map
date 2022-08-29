## 基本概念

1.Python文件是以.py结尾的。从技术上讲，这种命名方案在被“导入”时才是必须的，这也将在本书后边进行介绍，但绝大多数Python文件为了统一都是以.py命名的。[*Ref: 《Python学习手册》第4版 P38，机械工业出版社，Mark Lutz。*]()

2.在Linux及其他的UNIX类系统上使用Python，可以将Python代码编程为可执行程序，这样的脚本往往叫做可执行脚本且拥有如下两个特殊属性：

- 它们的第一行是特定的，以字符`#!`开始，其后紧跟机器Python解释器的路径，比如`#! /usr/local/bin/python`。不过这种硬编码Python安装路径的方式缺乏移植性，可以通过`#! /usr/bin/evn python`来允许env程序通过系统的搜索路径设置来定位Python解释器。
- 它们拥有可执行的权限。

但是，如果你可能想要在UNIX及WINDOWS系统中都运行文件，经常采用基本的命令行方法非UNIX风格的脚本去运行程序将更简单。

## 安装

python distribution 和 Anaconda, Spyder。


## Q&A

1）模块安装

使用matplotlib画线，本地测试无法找到该模块，那么可以使用 `pip3 install matplotlib`先安装。

如果在安装过程中提示网络问题，比如使用 `pip3 install pandas`安装时提示：

```
 Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x0000013C8C6942B0>, 'Connection to pypi.org timed out. (connect timeout=15)')': /simple/pandas/
```

就可以在安装时使用代理`pip3 --proxy 127.0.0.1:6152 install pandas`。

210922: 今天安装selenium，使用`pip3 --porxy http://127.0.0.1:6152 install selenium`成功，使用`pip3 --proxy 127.0.0.1:6152 install selenium`提示没有指定scheme，指定https提示“ValueError: check_hostname requires server_hostname”错误。

参考：

- [让 pip 走代理](https://www.logcg.com/archives/1914.html)


2）为什么安装了`selenium`但是import的时候一九提示“ModuleNotFoundError: No module named 'selenium'”

第一步执行`pip3 show selenium`查看`selenium`是否安装成功。

```
> pip3 show selenium
Name: selenium
Version: 3.141.0
Summary: Python bindings for Selenium
Home-page: https://github.com/SeleniumHQ/selenium/
Author: UNKNOWN
Author-email: UNKNOWN
License: Apache 2.0
Location: c:\users\lianbche\appdata\local\programs\python\python39\lib\site-packages
Requires: urllib3
Required-by:
```

在发现上面安装成功，并且重启编辑器尝试问题依然存在的时候，我们需要确认是否是因为电脑中安装了多个版本的Python，然后在Python A版本里安装`selenium`了，但是在运行程序的时候使用了Python B版本。那么如何确认呢？

首先在Windows下面搜索找到Python解析器打开，然后执行`import selenium`发现可以正常执行。现在命令行里面执行脚本发现不对那么基本肯定就是因为版本不匹配的问题。

通过`python -c "import os, sys; print(os.path.dirname(sys.executable))"`命令可以找到当前python调用的是`C:\msys64\mingw64\bin`下面的python。这也难怪通过`python -c "import sys; print(sys.path)"`的命令将系统的path打印出来，查看执行的Python里面是否包含了安装的`selenium`路径。

```
> python -c "import os, sys; print(os.path.dirname(sys.executable))"
C:\msys64\mingw64\bin

> python -c "import sys; print(sys.path)"
['', 'C:\\msys64\\mingw64\\lib\\python39.zip', 'C:\\msys64\\mingw64\\lib\\python3.9', 'C:\\msys64\\mingw64\\lib\\python3.9\\lib-dynload', 'C:\\N-xddks\\lianbche\\Downloads\\selenium-3.141.0', 'C:\\
msys64\\mingw64\\lib\\python3.9\\site-packages']
```

而如果搜索`selenium`发现安装在`C:\Users\lianbche\AppData\Local\Programs\Python\Python39\Lib\site-packages`，这样就确认了之所以运行python提示找不到模块的错误是因为模块的安装和当前程序的执行使用了不同的Python版本。

那么怎么解决这个问题？

在Linux上可以使用`alias`分别给不同版本的Python取别名并指向不同路径的Python版本。在Windows上最简单的方法就是把倾向版本的Path添加到系统变量的前面。可以看到这样调整之后一些相关的变量都会更新：

```
> python -c "import os, sys; print(os.path.dirname(sys.executable))"
C:\Users\lianbche\AppData\Local\Programs\Python\Python39

> python -c "import sys; print(sys.path)"
['', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Py
thon\\Python39\\lib', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']
```


参考：

- [ImportError: No module named 'selenium'](https://stackoverflow.com/questions/31147660/importerror-no-module-named-selenium)
- [How can I find where Python is installed on Windows?](https://stackoverflow.com/questions/647515/how-can-i-find-where-python-is-installed-on-windows)

## 基本概念

1.Python文件是以.py结尾的。从技术上讲，这种命名方案在被“导入”时才是必须的，这也将在本书后边进行介绍，但绝大多数Python文件为了统一都是以.py命名的。[*Ref: 《Python学习手册》第4版 P38，机械工业出版社，Mark Lutz。*]()

2.在Linux及其他的UNIX类系统上使用Python，可以将Python代码编程为可执行程序，这样的脚本往往叫做可执行脚本且拥有如下两个特殊属性：

- 它们的第一行是特定的，以字符`#!`开始，其后紧跟机器Python解释器的路径，比如`#! /usr/local/bin/python`。不过这种硬编码Python安装路径的方式缺乏移植性，可以通过`#! /usr/bin/evn python`来允许env程序通过系统的搜索路径设置来定位Python解释器。
- 它们拥有可执行的权限。

但是，如果你可能想要在UNIX及WINDOWS系统中都运行文件，经常采用基本的命令行方法非UNIX风格的脚本去运行程序将更简单。

## 安装

python distribution 和 Anaconda, Spyder。

当前server上有`3.6.8`和`3.8.13`两个版本，执行`python3`默认使用的是`3.6.8`，那么怎么切换到默认为`3.8.13`呢？

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.8
```

- [How to switch between Python 3 versions](https://dev.to/alfchee/how-to-switch-between-python-3-versions-5gh6)


## 查看当前已经安装的模块

```
help('modules')
```

查看版本信息，可以使用每个模块提供的`__version__`属性：

```
import pandas as pd

pd.__version__
pd.show_versions() #查看依赖模块的版本
```

如果安装了pip，那么使用`pip list`或者`pip3 list`可以查看所有安装的模块及对应的版本。

参考：

- [How do I get a list of locally installed Python modules?](https://stackoverflow.com/questions/739993/how-do-i-get-a-list-of-locally-installed-python-modules)
- [How to find the installed pandas version](https://stackoverflow.com/questions/20612645/how-to-find-the-installed-pandas-version)


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


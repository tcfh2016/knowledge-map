## 基本概念

1.Python文件是以.py结尾的。从技术上讲，这种命名方案在被“导入”时才是必须的，这也将在本书后边进行介绍，但绝大多数Python文件为了统一都是以.py命名的。[*Ref: 《Python学习手册》第4版 P38，机械工业出版社，Mark Lutz。*]()

2.在Linux及其他的UNIX类系统上使用Python，可以将Python代码编程为可执行程序，这样的脚本往往叫做可执行脚本且拥有如下两个特殊属性：

- 它们的第一行是特定的，以字符`#!`开始，其后紧跟机器Python解释器的路径，比如`#! /usr/local/bin/python`。不过这种硬编码Python安装路径的方式缺乏移植性，可以通过`#! /usr/bin/evn python`来允许env程序通过系统的搜索路径设置来定位Python解释器。
- 它们拥有可执行的权限。

但是，如果你可能想要在UNIX及WINDOWS系统中都运行文件，经常采用基本的命令行方法非UNIX风格的脚本去运行程序将更简单。


## 安装和`pip`工具

搭建Python开发的安装方式有如下几种：

1. 直接下载Python
2. 安装集成开发环境：`PyCharm`
3. 安装数据分析标准环境：`anaconda`
4. 安装文学式开发工具：`Jupyter Notebook`
5. 安装`IPython`

安装好Python开发环境之后，如果要安装其他依赖的包可以使用`pip`，这是一个通用的Python包管理工具。而`pip3`只是为了区分Python 2.x和Python 3.x而做了一些区分，如果电脑上仅仅安装了Python 3.x那么`pip`和`pip3`是一样的。

`pip`在安装Python的时候会自动安装，如果要升级执行下面的命令：

```
 C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe -m pip install --upgrade pip
```

参考：

- [安装python3后使用pip和pip3的区别是什么？](https://www.cnblogs.com/yymn/p/9353518.html)


## 切换Python版本

当前server上有`3.6.8`和`3.8.13`两个版本，执行`python3`默认使用的是`3.6.8`，那么怎么切换到默认为`3.8.13`呢？

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.8
```

- [How to switch between Python 3 versions](https://dev.to/alfchee/how-to-switch-between-python-3-versions-5gh6)


## 查看当前已经安装的模块

进入Python命令行，输入`help('modules')`可以查看当前已经安装好的各个模块。

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


## 模块安装

使用matplotlib画线，本地测试无法找到该模块，那么可以使用 `pip3 install matplotlib`先安装。

如果在安装过程中提示网络问题，比如使用 `pip3 install pandas`安装时提示：

```
 Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x0000013C8C6942B0>, 'Connection to pypi.org timed out. (connect timeout=15)')': /simple/pandas/
```

就可以在安装时使用代理`pip3 --proxy 127.0.0.1:6152 install pandas`。

210922: 今天安装selenium，使用`pip3 --porxy http://127.0.0.1:6152 install selenium`成功，使用`pip3 --proxy 127.0.0.1:6152 install selenium`提示没有指定scheme，指定https提示“ValueError: check_hostname requires server_hostname”错误。

进入Python命令行，输入`help('modules')`可以查看当前已经安装好的各个模块。


- [How do I get a list of locally installed Python modules?](https://stackoverflow.com/questions/739993/how-do-i-get-a-list-of-locally-installed-python-modules)
- [让 pip 走代理](https://www.logcg.com/archives/1914.html)


## 区分操作系统

有三种方式可以用来区分当前的操作系统，更推荐使用`platform.system()`因为它可以返回更加通用的名字。

```
sys.platform
# 'win32'  # could be 'linux', 'linux2, 'darwin', 'freebsd8' etc

os.name
# 'nt'  # for Linux and Mac it prints 'posix'

# platform.system()
'Windows' # For Linux it prints 'Linux'. For Mac, it prints `'Darwin'
```

参考：

- [How to identify which OS Python is running on](https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on/58071295)


## 技巧

- 使用`os.path.dirname(os.path.realpath(__file__))`来得到脚本执行时的绝对路径。
- 使用`sys.path.append(path)`来添加搜索路径。


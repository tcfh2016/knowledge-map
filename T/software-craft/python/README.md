## 内容索引

- [实践笔记]()
  - [类]()
  - [内建对象]()
  - [操作符]()
  - [字符串]()
  - [字符编码](./notes/char_encoding)
  - [文件]()
  - [控制流]()
  - [函数编程]()
  - [import语句]()
  - [urllib函数库]()
  - [tkinter图形库]()
  - [random函数库]()
  - [pickle函数库]()
  - [numpy函数库]()
  - [matplotlib函数库]()
  - [pandas函数库]()
  - [datetime函数库]()
  - [argparse函数库]()
  - [单元测试]()
  - [调试]()
- [工具箱]()
  - [文本搜索]()
  - [文本解析]()
  - [批处理]()


## Q&A

## 模块安装

使用matplotlib画线，本地测试无法找到该模块，那么可以使用 `pip3 install matplotlib`先
安装。

如果在安装过程中提示网络问题，比如使用 `pip3 install pandas`安装时提示：

```
 Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x0000013C8C6942B0>, 'Connection to pypi.org timed out. (connect timeout=15)')': /simple/pandas/
```

就可以在安装时使用代理`pip3 --proxy 127.0.0.1:6152 install pandas`。

参考：

- [让 pip 走代理](https://www.logcg.com/archives/1914.html)

## 编码规约

- 当你复制粘贴代码的时候，基本上都会使未来的维护工作倍增。考虑一下：如果最初的版本发生改
变，将修改两个地方的代码。当你试图按照这种复制代码的方式来编写程序的时候，可能需要考虑一
下有没有更好的方法。[*Ref: 《Python学习手册》第4版 P661，机械工业出版社，Mark Lutz。*]()

## 基本概念

1.Python文件是以.py结尾的。从技术上讲，这种命名方案在被“导入”时才是必须的，这也将在本书
后边进行介绍，但绝大多数Python文件为了统一都是以.py命名的。[*Ref: 《Python学习手册》第4
版 P38，机械工业出版社，Mark Lutz。*]()

2.在Linux及其他的UNIX类系统上使用Python，可以将Python代码编程为可执行程序，这样的脚本
往往叫做可执行脚本且拥有如下两个特殊属性：

- 它们的第一行是特定的，以字符`#!`开始，其后紧跟机器Python解释器的路径，比如`#! /usr/local/bin/python`。不过这种硬编码Python安装路径的方式缺乏移植性，可以通过`#! /usr/bin/evn python`
来允许env程序通过系统的搜索路径设置来定位Python解释器。
- 它们拥有可执行的权限。

但是，如果你可能想要在UNIX及WINDOWS系统中都运行文件，经常采用基本的命令行方法而非UNIX风
格的脚本去运行程序将更简单。

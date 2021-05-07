## import如何工作

`import x`中的模块名x起到两个作用：首先，识别加载的外部文档，也会变成赋值给被载入模块的
变量。其次，x定义的对象也会在执行时创建。Python的`import`语句并不同于C里的`#include`，
因为它并不是把一个文件文本插入到另一个文件，而是一种运行时运算，程序第一次导入指定文件时，
会执行三个步骤：*(注：使导入指定文件<模块>，而非目录<包>)*

- 搜索：找到模块文件。
  - Python使用标准模块搜索路径来找到对应模块，因此不需要指定路径和后缀名。
- 编译：编译成位码（需要时）。
  - Python会检查文件的时间戳，如果字节码文件比源代码旧那么程序运行时重新编译成字节码；
  - Python在搜索路径上只发现字节码而没有源代码时就会直接加载字节码；
  - 只有被导入的文件才会留下字节码文件.pyc，用来提高之后导入的速度；
  - 顶层文件通常是设计成直接执行，而不是被导入的，但一个文件即作为顶层文件又能被导入也是
  可能的。
- 运行：执行模块代码来创建其所定义的对象。

Python把载入的模块存储到`sys.modules`的表中，在导入操作之初便检查该表，如果模块不存在则
执行上述三个步骤并存储到该表，在下一次导入时便可以直接提取内存中已经加载的模块对象。

导入是一个开销很大的操作，以至于每个文件、每个程序运行不能够重复多于一次。如果要在一次会
话中再次运行文件（不停止和重新启动会话），需要调用reload函数。

## 模块搜索路径

Python的模块搜索路径（sys.path）是由四个组件组合而成：

- 程序的主目录：当你运行一个程序的时候，这个入口是包含程序的顶层脚本文件的目录；当在交互
模式下工作时，这个入口是当前工作目录。
- PYTHONPATH目录（如果已经进行了设置）：Python会从左至右搜索PYTHONPATH环境变量设置中列
出的所有目录，通常在导入文件处于不同目录时需要。
  - Windows上通过控制面板来设置名称为“PYTHONPATH”的环境变量；
- 标准库目录：Python会自动搜索标准库模块的安装目录。
- 任何.pth文件内容（如果存在的话）：Python会把文件每行所列的目录从头至尾添加到模块搜索路
径列表的最后，类似于PYTHONPATH。
  - .pth文件通常放置在Python安装目录的顶层或者标准库所在位置的sitepackages子目录。

搜索路径的配置可能随着平台及Python版本不同，如果要查看模块搜索路径的实际配置，可以通过打
印内置的`sys.path`列表来查看。它是在程序启动时进行配置，自动将顶级文件主目录、任何
PYTHONPATH、已经创建的任何.pth文件路径的内容以及标准库目录合并。

只有在跨目录进行导入时才需要模块搜索路径的设置。

如上第一条搜索规则决定了在 benchmark.py 中导入 strategy模块时不能简单的如C/C++一样使用
`import strategy`而是需要从工作目录开始搜索，即使用`import src.strategies.strategy
as strategy`才行。

```
C:.
│  line_parser.py
│
├─src
│  │  parser.py
│  │
│  ├─strategies
│  │  │  benchmark.py
│  │  │  maxrlc.py
│  │  │  strategy.py
```

*文件名后缀是可以从import语句中省略的，Python会选择在搜索路径中第一个符合导入文件名的文
件，它既可以是源代码文件x.py、字节码文件x.pyc、目录x或者其他编译扩展模块。*

如果你要import的模块不在搜索路径中，可以将其添加到sys.path里面。或者使用`os.chdir(target_directory)`切换新的工作目录。

```
import os
os.environ['PYTHONPATH'] #默认的路径

import sys
sys.path # Python的搜索路径
sys.path.append(target_directory)

```
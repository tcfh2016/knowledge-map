## 安装软件

最简单的就是在app store里面寻找并安装。

## 直接下载

很多软件在app store里面没有，所以需要去单独下载。在mac系统中对应的安装包有两种格式：`pkg`和`dmg`。

- 前者类似于Windows下面的exe需要双击打开安装
- 后者是一个虚拟磁盘文件，双击文件会打开访达，然后将对应应用拖到`application`

## 用`port`来安装软件

比如我需要安装python，首先执行`sudo port install python`来安装，会提示：

```
Warning: port definitions are more than two weeks old, consider updating them by running 'port selfupdate'.
Error: Port python not found
```

执行`port selfupdate`来更新好`port`。之后执行`port search python`来查找安装资源，找到最新的`python312 @3.12.1 (lang)`，执行`sudo port install python312`来安装。

安装完之后`sudo port select --set python python312`来将最新安装的`python312`设置为默认的python版本。

参考：

- [Homebrew、Fink、MacPorts三者对比](zhuanlan.zhihu.com/p/133595905)
- []()
## 用msys2来更新mingw64

今天尝试编译boost库，结果碰到了`'std::thread' has not been declared`的错误，查找原因后在[这里](https://github.com/boostorg/type_erasure/issues/16)看到了原因，似乎是因为本地的mingw版本太老，所以又需要更新mingw的版本。

当前使用的是4.3.5的版本，但在尝试更新mingw的过程中发现对应的installer似乎不再可用，要么通过源代码进行编译（复杂），要么使用msys2来进行更新。

msys2的操作共下面几步：

1. 下载msys2并安装，默认选项即可。安装完选择运行msys2会弹出命令行窗口。

2. 执行`pacman -Syu`来更新软件包数据库和基础软件包

这一步的时候碰到了代理问题，仿照[How to easily set a proxy after installing MSYS2 on Windows 7 ?](https://sourceforge.net/p/msys2/discussion/general/thread/96099494/)里面的方式到"C:\msys64\etc"里面将代理的设置添加到了profile文件里面，然后执行上面命令可以正常更新。

```
# Proxy Setting
export HTTP_PROXY="IpAddress:Port" # Like: 127.0.0.1:1477
export HTTPS_PROXY=$HTTP_PROXY
export http_proxy=$HTTP_PROXY
export https_proxy=$HTTP_PROXY
```

![](run-pacman-syu.png)


3. 执行`pacman -Su`更新其他软件包数据库

4. 执行`pacman -Ss mingw`安装mingw

这一步执行`pacman -Ss mingw`没有成功，而是按照[官方文档](https://www.msys2.org/)里的`pacman -S --needed base-devel mingw-w64-x86_64-toolchain`完成了mingw的安装。晚装完了之后将“C:\msys64\mingw64\bin”路径填写到系统环境变量Path里，并删除了之前的mingw目录。


参考：

- [Installing the latest version of mingw-w64 on Windows](https://stackoverflow.com/questions/61497394/installing-the-latest-version-of-mingw-w64-on-windows)
- [How to install MinGW-w64 and MSYS2?](https://stackoverflow.com/questions/30069830/how-to-install-mingw-w64-and-msys2)
- [MSYS2](https://www.msys2.org/)
- [MSYS2 - How to set proxy settings in msys2](https://gist.github.com/vheidari/cf7be91dcc522c388488552a59e22049)

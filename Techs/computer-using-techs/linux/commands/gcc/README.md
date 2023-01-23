## gcc的编译选项

-c  生成.o，不进行链接；
-o 选项是将所有文件输出为一个最终文件，当然可以在任何阶段添加；
-S 生成.s，不进行汇编；
-E 会将经过预处理之后的源文件打印到标准输出（即屏幕），可以使用重定向来保存。


其实对于上面的每个选项，gcc编译驱动器仅仅是分别调用了不同阶段的工具，依次对应cpp, cc1(cc1plus), as, ld。而合阶段生产文件后缀名也通常约定为.i, .s, .o, .out。


## cc1plus错误

今天在实验的时候用gcc来编 译.cpp碰到提示“cc1plus”的错误，在网上搜索资料发现是对应的编译器没有安装（gcc在编译和g++在编译的时候都是调用的cc1plus， 或者说gcc实际上是使用的g++，因为之前gcc只是编译c的，之后可以支持编译其他开发语言），通过sudo apt-get install build-essential安装编译用的基本所有编译器即可行。

只是上面碰到另外一个问题，提 示“E:Encountered a section with no Package: header ... E:The package lists or status file could not be parsed or opened.”的错误，也就是在安装的时候软件包处理的流程上有问题（对于这个apt-get具体怎么一个处理流程不熟悉）。可以肯定的是，这是由于本 地package目录存储引起的问题，在用update manager, apt-get,synaptic等命令的时候会出现上面的问题。

最终解决：

1. 执行下面的命令，删除一些东西

```
sudo rm -rf /var/lib/apt/lists
sudo mkdir /var/lib/apt/lists
sudo mkdir /var/lib/
apt/lists/partial
```

2. 重新执行`apt-get install build-essential`更新，顺便把该更新的软件都更新了。之后解决。
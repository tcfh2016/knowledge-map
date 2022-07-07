## 常用命令

查看当前的linux系统版本信息：

- `uname -a`：查看内核版本信息
- `cat /etc/os-release`：查看release信息
- `hostnamectl`：查看系统hostname及相关设置

参考：[How to check os version in Linux command line](https://www.cyberciti.biz/faq/how-to-check-os-version-in-linux-command-line/)

## home 目录下的core文件

当系统有一些低级的crash（一些应用程序执行时的crash）的时候会在home目录下面生成core文件，但这首先取决于系统本身的配置，可以通过`ulimit -c`查看当前配置，该命令是用户可以使用的系统资源。设置为0那么就不会产生core文件，因为没有空间资源来存放，如果是unlimited那么就没有问题。

可以通过`gdb -c corefile`，或者使用`file corefile`命令来查看是哪个程序crash产生的core文件。找到对应程序之后，可以通过[core files in home folder?](https://www.reddit.com/r/voidlinux/comments/hn3qvy/core_files_in_home_folder/)这里提到的命令来打开查看调用栈：

```
$ gdb /usr/bin/Xwayland ~/core.1442
(gdb) bt full
```

参考：

- [A big core dump appeared in my home folder - what is it and how can I delete it?](https://askubuntu.com/questions/800416/a-big-core-dump-appeared-in-my-home-folder-what-is-it-and-how-can-i-delete-it)

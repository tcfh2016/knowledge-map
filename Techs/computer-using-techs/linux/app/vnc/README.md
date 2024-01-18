## 安装

如果当前系统没有安装vncserver，也就是你在执行命令时会提示“vncserver: command not found”，那么可以执行`yum install vnc-server`来安装。

但安装完成之后还是启动不了，后面安装`yum install tigervnc-server`之后解决问题。

参考：

- [Installed vncserver, but cannot start it](https://www.linuxquestions.org/questions/linux-newbie-8/installed-vncserver-but-cannot-start-it-4175497246/)

## 常用命令

- 如果要查询已经创建的vnc session，使用`vncserver -list`
- 删除某个session，使用`vncserver -kill :5`

参考：

- [About Linux VNC Sessions](https://peden.ece.uw.edu/computing/linux-vnc-sessions/)


##

使用`vncserver`创建用户之后，刚连接便失败，之后解决是在[Bug 1646889 - Tigervnc not starting on RHEL 7.6 server without -noxstartup option](https://bugzilla.redhat.com/show_bug.cgi?id=1646889)看到添加了`-noxstartup`的参数来解决。

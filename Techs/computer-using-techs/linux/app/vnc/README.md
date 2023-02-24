## 常用命令

- 如果要查询已经创建的vnc session，使用`vncserver -list`


参考：

- [About Linux VNC Sessions](https://peden.ece.uw.edu/computing/linux-vnc-sessions/)


##

使用`vncserver`创建用户之后，刚连接便失败，之后解决是在[Bug 1646889 - Tigervnc not starting on RHEL 7.6 server without -noxstartup option](https://bugzilla.redhat.com/show_bug.cgi?id=1646889)看到添加了`-noxstartup`的参数来解决。

## 配置快捷键

从`Setup tasks`创建一个ssh的连接：

```
set "PATH=%ConEmuDir%\..\git-for-windows\usr\bin;%PATH%" & %ConEmuDir%\..\git-for-windows\usr\bin\ssh ubuntu@remote_address -new_console:d:%USERPROFILE% "-new_console:t:[dev.tencent]"
```

参考：

- [Cmder - Build SSH connection quickly](https://medium.com/@erinus/cmder-setup-tasks-e5109bbb742b)
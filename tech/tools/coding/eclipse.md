## 常用快捷键

```
alt + shift + r   # 重命名
ctrl + <          # 前一步
ctrl + >          # 后一步
ctrl + shife + T  # 搜索工程中的类/函数/变量。
ctrl + shife + R  # 搜索工程中的文件。
ctrl + o          # 在本文件内搜索函数。
ctrl + shift + h  # 搜索调用。
ctrl + shift + g  # 搜索文本所在的文件。

ctrl + shift + P  # 找到对应的括号。
ctrl + Y          # 重做。
ctrl + /          # 注释，再按取消。
F3                # 调到声明处。
```

## 在RedHat上通过命令`eclipse`启动eclipse出现“Workspace in use or cannot be created”的错误：

![](eclipse_workspace_unavailable.png)

之前没有遇到类似的问题，google之后在StackOverflow上找到解决方法：

> Just delete the .lock file in the .metadata directory in your eclipse workspace directory

问题背后原理暂未作了解，目前推测是与异常退出有关。

参考：

- [Eclipse says: “Workspace in use or cannot be created, chose a different one.” How do I unlock a workspace?](https://stackoverflow.com/questions/8489322/eclipse-says-workspace-in-use-or-cannot-be-created-chose-a-different-one-ho)
- [Eclipse - “Workspace in use or cannot be created, chose a different one.”](https://stackoverflow.com/questions/7465793/eclipse-workspace-in-use-or-cannot-be-created-chose-a-different-one)

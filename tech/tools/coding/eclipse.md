## 在RedHat上通过命令`eclipse`启动eclipse出现“Workspace in use or cannot be created”的错误：

![](eclipse_workspace_unavailable.png)

之前没有遇到类似的问题，google之后在StackOverflow上找到解决方法：

> Just delete the .lock file in the .metadata directory in your eclipse workspace directory

问题背后原理暂未作了解，目前推测是与异常退出有关。

参考：

- [Eclipse says: “Workspace in use or cannot be created, chose a different one.” How do I unlock a workspace?](https://stackoverflow.com/questions/8489322/eclipse-says-workspace-in-use-or-cannot-be-created-chose-a-different-one-ho)
- [Eclipse - “Workspace in use or cannot be created, chose a different one.”](https://stackoverflow.com/questions/7465793/eclipse-workspace-in-use-or-cannot-be-created-chose-a-different-one)

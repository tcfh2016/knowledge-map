## Mac Air重装

第一次接触mac系统，从家里领导手里接过来的，想着重置下给我自己用。于是照着网上的教程将“Macintosh HD”内容删除。删除的同时也分不清“Macintosh HD”, "Macintosh HD - 数据"，“macOS Base System”它们到底是啥？

结果执行擦除之后就傻眼了，因为系统启动不起来了，启动的时候扇动一个带问号的文件夹图标。然后继续仿照网络上的文章安装系统，但是总体提示“未能与恢复服务器取得联系”，之后分别尝试了下面几种方法：

- 修改时间为“UTC”
- 修改输入法为“简体中文”

但是均失败。


## 理解磁盘

特别是要了解“Macintosh HD”, "Macintosh HD - 数据"和“macOS Base System”分别是什么？

我最初是直接把“Macintosh HD”干掉，然后发现无法重启启动系统，但是因为误以为“macOS Base System”是系统盘，而查看它的大小依然有1个多G，所以认为我没有动系统盘，为什么会遇到启动问题呢？但实际上，自己的认识是错误的。

Mac系统下的启动盘就是“Macintosh HD”，存放用户数据的是“Macintosh HD - 数据”，而磁盘映像“macOS Base System”是一个“只读”的磁盘映像，它里面包括了恢复Mac系统的软件信息以及磁盘工具。

“Macintosh HD”是Mac开机之后自动加载的系统，当“Macintosh HD”不能工作时，“macOS Base System”可以用来重置系统。


## 接下来的操作

在我的内置宗卷里面有“Macintosh HD - 数据”和“update”两个宗卷，没有“Macintosh HD”。我按照[]()里面提到的删除“update”宗卷，并且重新抹掉“Macintosh HD - 数据”并将其重命名为“Macintosh HD”

参考：

- [最详细的重装macOS系统教程](https://zhuanlan.zhihu.com/p/349009503)
- [What Is macOS Base System [Everything You Need to Know]](https://www.easeus.com/knowledge-center/what-is-macos-base-system.html)
- [What is macOS Base System?](https://iboysoft.com/wiki/mac-os-base-system.html)
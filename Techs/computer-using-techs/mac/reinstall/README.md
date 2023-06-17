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


## 组合键的不同

重新阅读[如何重新安装 macOS](https://support.apple.com/zh-cn/HT204904)，看到原来组合键还有玄机，比如：

- command + r：进入恢复模式启动，重新安装一直提示“未能与恢复服务器取得联系”。
- 启动过程中使用 Option-Command-R，你可能会获得与 Mac 兼容的最新版 macOS。尝试后会有个地球出来转圈，然后也会进度条并提示“正在开始互联网恢复”。能够正常进行安装。
- 启动过程中使用 Shift-Option-Command-R，你可能会获得 Mac 自带的 macOS 或者与它最接近且仍在提供的版本。


## 安装“macOS Monterey”

选择磁盘时有“Macintosh HD”和“I”两个选项，实际上大小都是一样，不知道多出来的那个“I”是哪里来的。

第一次安装提示“PKdownload失败，错误码8”，重新试了一次，慢慢的就成功了。


参考：

- [最详细的重装macOS系统教程](https://zhuanlan.zhihu.com/p/349009503)
- [What Is macOS Base System [Everything You Need to Know]](https://www.easeus.com/knowledge-center/what-is-macos-base-system.html)
- [What is macOS Base System?](https://iboysoft.com/wiki/mac-os-base-system.html)
- [如何重新安装 macOS](https://support.apple.com/zh-cn/HT204904)
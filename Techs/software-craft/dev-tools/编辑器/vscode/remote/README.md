## 远程开发

## SSH远程开发和WSL（Windows Subsystem for Linux）开发

这两天使用VSCODE用SSH连接远端服务器进行开发，在阅读了解的过程中一直不明白用SSH远端开发和WSL有什么区别，感觉上是一样的啊？

在阅读了[WSL + VS Code Remote真香](https://juejin.cn/post/6844904021216460808)和[Remote Development with VS Code](https://code.visualstudio.com/blogs/2019/05/02/remote-development)之后有些理解了WSL相当于在Windows下面创建了虚拟机进行开发，即在Windows下面构建了Linux的开发环境。也就是：

- Remote-WSL：在Windows上面虚拟出Linux环境进行开发
- Remote-SSH: 连接到远端服务器进行开发
- Remote-Container：连接Docker容器进行开发

所以，我当前仅仅需要一个Remote-SSH就够了。


## 使用ssh登录远程服务器进行开发

官方使用说明在这里：[VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)。

首先要做的是安装“Remote - SSH”插件，安装好了之后就可以连接远程的服务器，连接成功后在左下角会有状态展示。此时打开terminal也默认是远程的终端。

![](ssh-link-status.png)

其次是设置ssh publickey，因为每次认证输入用户名密码比较麻烦。所以需要在远程服务器上添加客户端的publickey。在[这里](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)找到了将客户端的publickey添加到远端服务器上的方式，最简单的方案是将客户端的id_rsa.pub里面的内容拷贝到服务器上的authorized_keys里面（如果没有就新建一个，`~/.ssh/authorized_keys`）。但执行后发现如下错误：

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions for 'C:\\Users\\lianbche/.ssh/id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "C:\\Users\\lianbche/.ssh/id_rsa": bad permissions
lianbche@ip_address's password:
```

在[Windows SSH: Permissions for 'private-key' are too open](https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open)找到答案，解决方式和上面的问题类似，也即是将`C:\Users\lianbche\.ssh\id_rsa`的权限先disable inheritance并删除所有的权限，然后仅仅给自己分配full control的权限即可。


如果已经配置了公钥但是还是提示输入用户名密码，那么需要去修改`/etc/ssh/sshd_config`里面的配置，将`PasswordAuthentication yes`修改为`no`。让该修改生效还需要执行`sudo systemctl restart ssh`来重启ssh服务。

之后再次连接发现还是不成功，提示“Permission denied (publickey,gssapi-keyex,gssapi-with-mic)”，按照参考链接中的文章设置了下面权限才成功了。

```
#chmod 700 ~/.ssh
#chmod 644 ~/.ssh/authorized_keys
```

其他参考：

- [Remote development over SSH](https://code.visualstudio.com/docs/remote/ssh-tutorial)
- [ssh免密码登录Permission denied (publickey,gssapi-keyex,gssapi-with-mic) 的解决方案！](https://www.cnblogs.com/xubing-613/p/6844564.html)

## Q&A

1）安装远程插件失败后如何进行手动安装？

今天尝试通过远端开发来调试脚本，在浏览Python代码的时候VSCODE提示remote安装Python插件，尝试安装的时候发现timeout并提示手动安装。

点击提示链接下载了一个名称为“ms-python.python-2021.9.1246542782.vsix”的插件文件。然后在插件说明上面查找链接并找到了[Install from a VSIX](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix)，这似乎就是我想要的手动安装指南。上面提供了下面几种安装方式：

- 在插件菜单选项里使用“Install from VSIX”命令
- 或者直接在Command Palette上使用“Extensions: Install from VSIX”命令
- 也可以直接使用VS CODE的“--install-extension”命令：`code --install-extension myextension.vsix`

![](./install_from_VSIX.PNG)

然后定位到下载的vsix文件，安装即可。

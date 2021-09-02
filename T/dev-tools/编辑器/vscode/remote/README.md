## 远程开发


## 使用ssh登录远程服务器进行开发

官方使用说明在这里：[VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)。

首先要做的是安装“Remote - SSH”插件，安装好了之后就可以连接远程的服务器，连接成功后在左下角会有状态展示。此时打开terminal也默认是远程的终端。

![](ssh-link-status.png)

其次是设置ssh publickey，因为每次认证输入用户名密码比较麻烦。所以需要在远程服务器上添加客户端的publickey。在[](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)找到了将客户端的publickey添加到远端服务器上的方式，但执行后发现如下错误：

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

其他参考：

- [Remote development over SSH](https://code.visualstudio.com/docs/remote/ssh-tutorial)

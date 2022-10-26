## SSH

## ssh连接失败

在Windows下面使用 `ssh username@serverip`的方式连接得到如下错误，但是使用putty是可以的：

```
PS C:\Users\lianbche> ssh lianbche@10.183.74.220
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:bIemjDG4biq1Ep0ndYR4IxwsrQCX7P8ZdJJ+xmPQ420.
Please contact your system administrator.
Add correct host key in C:\\Users\\lianbche/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in C:\\Users\\lianbche/.ssh/known_hosts:11
ECDSA host key for 10.183.74.220 has changed and you have requested strict checking.
Host key verification failed.
```

打开`.ssh/known_hosts`，然后删除对应IP的条目，重新链接，成功。


## SSH publickey

在访问代码仓库的时候如果提示“Permission denied (publickey)”的错误，那么可能是SSH没有设定，此时需要在访问的设备上使用命令`cd ~/.ssh && ssh-keygen`生成SSH公钥并拷贝到被访问服务器上：

参考：

- [Git: How to solve Permission denied (publickey) error when using Git?](https://stackoverflow.com/questions/2643502/git-how-to-solve-permission-denied-publickey-error-when-using-git)

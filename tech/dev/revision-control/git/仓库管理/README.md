## 仓库克隆 / git clone

在克隆远程仓库时支持两种连接方式：SSH和HTTPS。

```
git clone git@XXX.com:lte/remote_repository.git
git clone https://XXX.com/remote_repository.git
```

无论哪种方式均需进行用户名、密码验证，你可以通过配置SSH Key来简化验证过程。当连接可用，
但是验证失败时，会提示如下失败。此时可以通过确认用户名密码是否正确以及添加SSH Key来解决。

```
Cloning into 'repository'...
remote: HTTP Basic: Access denied
fatal: Authentication failed for 'https://XXX.com/lte/repository.git/'
```

如果当前系统屏蔽了git，那么你可能遇到如下错误：

```
Cloning into 'repository'...
fatal: unable to access 'https://XXX.com/lte/repository.git/': Failed to connect to github.com port 443: Timed out
```

这个时候通常需要给git配置代理，由于当前并没有对应的仓库存在，因此必须设定全局配置：`> git config --global http.proxy http://222.222.222.222:8080`。


## 设置代理 / config proxy

这个操作之前用过，但现在基本上国内可以自由访问，使用得也少。为git设定代理使用如下命令：

```
> git config --global http.proxy http://222.222.222.222:8080
> git config --global https.proxy https://222.222.222.222:8080
> git config --global --unset http.proxy
> git config --global --unset  https.proxy
```

后面两条命令是取消代理设置。

*注：需要同时设置http, https。*


## 远端仓库与本地仓库 / git remote

在将一个远端仓库克隆到本地的时候，我们便拥有了同一个仓库的两份数据，存放本地的可以称之为
“local repository”，远端的唯一镜像称之为“remote repository”。之后在本地修改所做的`git add`
以及`git commit`等操作都是针对“local repository”，要让远端的同步这些修改那么就要用到
`git push`操作。

- 查看`remote repository`

```
> git remote -v
```

- 添加`remote repository`

```
> git add "repository address"
```

## 原始仓库、远端仓库与本地仓库 / git fork

在folk了其他仓库（设为"original repository）"之后，并将folk之后的仓库（“remote repository”）
克隆到本地(“local repository”)，此时相当于同时拥有了同一个仓库的三份数据。此时“original repository”是独立在前两者关系之外的，这时需要通过添加“upstream关系”来为“original repository”和“remote repository”之间建立连接。

```
> git remote add upstream https://github.com/samuel/python-ping.git
```

之后，通过`git remote -v`能够查看这三者之间的关系：

```
F:\Coding\PythonPorjects\python_ping\python-ping>git remote -v
origin XXX/bing/python-ping.git (fetch)
origin XXX/bing/python-ping.git (push)
upstream XXX/samuel/python-ping.git (fetch)
upstream XXX/samuel/python-ping.git (push)
```

- 向下更新

即将“original repository”里面的修改同步到"remote repository"和"local repository"。

```
> git fetch upstream # 获取orginail repository的修改。
> git merge upstream/master # 将orginail repository的修改合并到local repository。
```

- 向上更新

向上更新分两步走：一，先将本地的修改推送到remote repository；二，发起`pull request`将
“remote repository”的修改提交给“original repository”。

- git fetch 提示RSA host key过时

```
[lianbche@hzlinb17 fddmac]$ git fetch  origin
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@       WARNING: POSSIBLE DNS SPOOFING DETECTED!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
The RSA host key for git-macps.dynamic.nsn-net.net has changed,
and the key for the corresponding IP address 10.159.90.30
is unknown. This could either mean that
DNS SPOOFING is happening or the IP address for the host
and its host key have changed at the same time.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that the RSA host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
77:8c:8d:3a:96:23:ff:3c:98:47:78:70:ea:bd:5e:be.
Please contact your system administrator.
Add correct host key in /home/lianbche/.ssh/known_hosts to get rid of this message.
Offending key in /home/lianbche/.ssh/known_hosts:11
RSA host key for git-macps.dynamic.nsn-net.net has changed and you have requested strict checking.
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

使用`ssh-keygen -l -f ~/.ssh/known_hosts`查看本地存储的针对远端服务器的认证信息，然后
使用`ssh-keygen -R 服务器端的ip地址/url地址`移除指定hostname的key，再重新执行`get fetch origin`命令即可。

```
[lianbche@hzlinb17 fddmac]$ ssh-keygen -R git-macps.dynamic.nsn-net.net
/home/lianbche/.ssh/known_hosts updated.
Original contents retained as /home/lianbche/.ssh/known_hosts.old
[lianbche@hzlinb17 fddmac]$ ssh-keygen -l -f ~/.ssh/known_hosts
1024 d4:28:1b:1d:e3:6a:15:bc:53:07:41:2a:02:94:40:6f [hztddgit.china.nsn-net.net]:29418,[10.140.20.32]:29418 (RSA)
2048 12:55:33:83:4b:a4:dc:5a:d5:d5:1f:33:d6:91:f0:3c ulling06.emea.nsn-net.net,10.159.34.13 (RSA)
1024 d4:28:1b:1d:e3:6a:15:bc:53:07:41:2a:02:94:40:6f [hzling15.china.nsn-net.net]:29418,[10.159.194.4]:29418 (RSA)
2048 b1:ef:11:20:0f:08:b1:fe:b8:e5:a5:b7:fb:6f:af:1e eagle393,10.46.209.93 (RSA)
2048 72:66:10:c9:d2:69:07:7a:49:87:f4:6a:66:e1:65:5e 10.56.78.176 (RSA)
2048 ba:76:4e:32:ca:13:ee:c6:11:6b:98:38:4c:0c:a9:62 hzlinb33.china.nsn-net.net,10.159.111.68 (RSA)
2048 92:8a:8f:78:c4:15:92:2d:ee:bd:90:bc:72:0a:59:76 hzlinb17.china.nsn-net.net,10.159.218.90 (RSA)
2048 c0:25:67:d7:14:ef:17:48:ae:ce:85:52:63:dc:39:13 wrlinb101.emea.nsn-net.net,10.159.92.138 (RSA)
2048 3b:a6:16:cc:91:52:3c:5f:56:7c:14:e5:b9:fd:7e:df 10.42.180.193 (RSA)
1024 d4:28:1b:1d:e3:6a:15:bc:53:07:41:2a:02:94:40:6f [10.159.218.28]:29418 (RSA)
256 a5:8a:48:d0:3c:98:e2:15:17:3a:da:50:43:43:88:3b 10.42.180.80 (ECDSA)
2048 42:9b:e5:fe:ff:5a:a2:10:b3:81:be:aa:c8:c3:a5:42 10.56.78.188 (RSA)
2048 42:9b:e5:fe:ff:5a:a2:10:b3:81:be:aa:c8:c3:a5:42 10.106.211.28 (RSA)
2048 42:9b:e5:fe:ff:5a:a2:10:b3:81:be:aa:c8:c3:a5:42 10.106.211.22 (RSA)
2048 42:9b:e5:fe:ff:5a:a2:10:b3:81:be:aa:c8:c3:a5:42 10.106.211.23 (RSA)
```

参考

- [ssh-keygen 维基百科](https://zh.wikipedia.org/wiki/Ssh-keygen)
- [ssh-keygen OpenBSD](http://man.openbsd.org/OpenBSD-current/man1/ssh-keygen.1#NAME)

## 添加远端仓库

在添加远端仓库时不仅支持URL还支持相同服务器的目录寻址，比如：

```
git remote add new_remote_name /home/lianbche/fddmac
git fetch new_remote_name trunk:remotes/new_remote_name/trunk
```

如上的操作分为两步：首先，添加名称为`new_remote_name`的远端仓库，该仓库与目录`/home/lianbche/fddmac
`关联；其次，将远端仓库的`trunk`分支与本地仓库`trunk`关联。

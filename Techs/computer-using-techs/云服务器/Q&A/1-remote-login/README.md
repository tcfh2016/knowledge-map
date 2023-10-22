## 远程登录

在购买之后云服务之后首先只能通过浏览器打开控制台进行操作，如果要进行远端登录那么首先需要创建对应的账号，然后设定密码才能登陆。或者使用默认的用户名和密码进行登陆。当然，登陆的方式可以选择密码的方式，也可以选择使用公钥的方式。

登陆的时候可以用`useradd`, `passwd`创建新用户，我创建的时候还碰到了系统没有默认创建用户目录，使用root创建后还需要使用`chown`和`chgrp`来修改。


## vscode remote

今天用工作PC来登录服务器，发现一直提示“https://blog.csdn.net/qq_39448884/article/details/124562118”的错误，搜索之下解决步骤为：

- 在服务器的home目录下面的`.vscode-server`目录下面找到对应这次登录的`${COMMIT_ID}`
- 然后在`https://update.code.visualstudio.com/commit:${COMMIT_ID}/server-linux-x64/stable`链接下载`vscode-server-linux-x64.tar.gz`
- 使用filezilla将该压缩包上传到服务器`.vscode-server`下对应的`${COMMIT_ID}`目录解压
- 重新连接，成功。

参考：

- [](https://blog.csdn.net/qq_39448884/article/details/124562118)
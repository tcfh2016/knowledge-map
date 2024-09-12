## 仓库克隆 / git clone

在克隆远程仓库时支持两种连接方式：SSH和HTTPS。

```
git clone git@XXX.com:lte/remote_repository.git
git clone https://XXX.com/remote_repository.git
```

无论哪种方式均需进行用户名、密码验证，你可以通过配置SSH Key来简化验证过程。当连接可用，但是验证失败时，会提示如下失败。此时可以通过确认用户名密码是否正确以及添加SSH Key来解决。

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


## 更新仓库地址

有一天，我觉得之前创建仓库的名字不好听了，所以想修改仓库名字，同时将对应仓库地址也更新掉。这里“更新仓库名字”和“更新仓库链接地址”是两回事：

- 创建仓库的时候，这个链接地址是直接根据仓库名字转换过来的。比如最开始创建的仓库名字为`repo`，那么生成的仓库链接地址就为`https://github.com/user/repo.git`。
- 之后，想要修改仓库名称的时候，你可以直接修改仓库名字，但链接地址并不会自动更新。如果要修改，需要手动修改。

那么怎么做呢？在[How to change the URI (URL) for a remote Git repository?](https://stackoverflow.com/questions/2432764/how-to-change-the-uri-url-for-a-remote-git-repository)给出了一个很好的示例，使用`set-url`命令：

```
git remote -v
# origin  https://github.com/user/repo.git (fetch)
# origin  https://github.com/user/repo.git (push)

git remote set-url origin https://github.com/user/repo2.git
# Change the 'origin' remote's URL

git remote -v
# origin  https://github.com/user/repo2.git (fetch)
# origin  https://github.com/user/repo2.git (push)
```

## 如何基于本地已有的文件创建新的仓库

在github/gitlab上面新建一个新的仓库，会有下面的提示命令，使用它就可以直接在本地新建仓库，然后push到github：

```
cd existing_folder
git init
git remote add origin git@bhgitlab.ext.net.nokia.com:lianbche/sg08scriptrepo.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

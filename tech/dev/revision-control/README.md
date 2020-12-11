## 索引

- [仓库管理]()
- [分支管理]()
- [修改管理]()

## 常见问题

1）执行`git remote -v`的时候能够看到多个同名的但是不一样url的remote仓库

这种情况可能与配置文件有关，比如在`~/.gitconfig`下是默认的全局配置文件，然后在本地仓库目录的`.git/config`下面设置了该仓库对应的一些配置，然后两边配置文件里面融合之后可能造成该现象。解决方案是清理掉全局配置里面设定的remote信息即可。

```
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[remote "origin"]
        url = https://xxx.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
[user]
        name = xxx
        email = xxx@gmail.com
```

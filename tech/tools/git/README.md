# Git使用笔记

## 提交人信息设置 / config committer

在本地克隆了一个`remote repository`之后，你开始在本地工作，然后将产生的新的修改`push`
到`remote repository`，在这之前你需要先配置提交人信息，这里有两类配置：

- local 配置

```
> git config user.name tcfh2016
> git config user.email tcfh2016@gmail.com
```

此种配置仅对当前工程生效。如果你需要为不同的仓库使用不同的提交人信息，那么这种设置是方便
的。

- global 配置

```
> git config --global user.name tcfh2016
> git config --global user.email tcfh2016@gmail.com
```

此种配置对当前系统里所有工程生效。

配置完成之后你可以通过 `git config -l `命令来查看当前仓库的所有配置，其中包括了committer
的设置。

## 提交人信息修改 / amend author

当你发现在当前仓库commit的修改使用了你不想使用的committer信息时，你可以通过三个步骤来修
改它。

Step1：使用`git rebase -i SHA1`将修改的commit囊括进来，这里SHA1需要指定你需要修正的那
条commit的前一条。

Step2：修改弹出的编辑框内的你需要修改的那条记录前的`pick`为`edit`，保存并退出。

Step3：使用`git commit --amend --author="tcfh2016 <tcfh2016@gmail.com>"`来完成修改。

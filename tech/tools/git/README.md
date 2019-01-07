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
`local repository`，远端的唯一镜像称之为`remote repository`。之后在本地修改所做的`git add`
以及`git commit`等操作都是针对`local repository`，要让远端的同步这些修改那么就要用到
`git push`操作。

- 查看`remote repository`

```
> git remote -v
```

- 添加`remote repository`

```
> git add "repository address"
```

## 远端分支与本地分支 / git branch

在将一个远端仓库克隆到本地的时候，我们便拥有了同一个仓库的两份数据。一个仓库可以拥有多个
分支，但在仓库最开始创建的时候仅有一个分支，并且默认远端分支名称为`origin`，本地分支默认
名称为`master`。

- 查看当前的分支使用如下命令

```
> git branch
```

如果要查看当前分支对应的远程分支用`git branch -vv`，即只需要加上`-vv`参数即可。

- 将本地分支的改动推送到远端分支

```
> git push "remote branch" "local branch"
```

如果觉得每次都执行分支名称过于繁琐，那么可以通过`git push -u origin mater`来设定便捷记
忆：在使用了`-u`参数之后，以后只需要键入`git push`即默认执行`git push -u origin mater`。

## 取消已经生效的修改

我们将“已经生效”分为如下三种情况：一，执行`git add`之后暂存的修改；二，执行`git commit`
之后在本地分支生效的修改；三，执行`git push`已经在远端分支生效的修改。

- 回退`git add`暂存的修改

```
git reset "file or directory"
```

通常来说，已经改动但是没有执行`git add`的文件处于“unstaged”状态，执行`git add`之后便处
于"staged"状态。因此，这里的前一个命令是将"staged"状态的文件回退到"unstaged"状态，处于
“unstaged”状态的文件可以直接通过`git checkout`来还原。

- 回退本地分支生效的修改

```
git reset SHA-0
git reset --hard SHA-0
```

假设本地修改在`git commit`之后的提交记录为SHA-1，它前一个提交为SHA-0，那么使用前一个命
令可以将SHA-1的修改回退到`unstaged`状态。后一个命令会直接删除SHA-1的修改。

- 回退远端分支生效的修改

远端分支已经生效的修改只能通过本地回退，再推送到远端。

方式一：执行`git revert SHA1`在本地回退修改，再执行`git push`推送到远端。

方式二：执行`git rebase -i SHA2`并删除掉SHA1的那次修改（注：SHA2是SHA1的前一个分支），
再执行`git push`推送到远端。

## 获取更新 / git pull

`git pull` 相当于`git fetch`和`git merge FETCH_HEAD`。


## 远端分支与本地分支 / git branch

在将一个远端仓库克隆到本地的时候，我们便拥有了同一个仓库的两份数据。一个仓库可以拥有多个
分支，但在仓库最开始创建的时候仅有一个分支，并且默认远端分支名称为`origin`，本地分支默认
名称为`master`。

### 查看当前的分支使用如下命令

```
> git branch
```

如果要查看当前分支对应的远程分支用`git branch -vv`，即只需要加上`-vv`参数即可。

### 将本地分支的改动推送到远端分支

```
> git push "remote branch" "local branch"
```

如果觉得每次都执行分支名称过于繁琐，那么可以通过`git push -u origin mater`来设定便捷记
忆：在使用了`-u`参数之后，以后只需要键入`git push`即默认执行`git push -u origin mater`。


### -f/--force

下面的命令是什么含义？

```
git checkout -b adaptation/psint origin/adaptation/psint
git checkout -b tmp
git branch -f adaptation/psint 1548a61fb4cfe6a3ec1350a5ae79025bf2785cf1
git rebase --onto tmp dd7b07ec357ced96a813471e75e7941e9671db5f~1 adaptation/psint -i
```

先基于远端分支创建本地分支，创建临时分支，再将本地分支reset到对应的SHA。这里之所以要创建
临时分支是因为无法对当前分支进行force update。

参考：

- [Checkout a New Branch or Reset a Branch to a Start Point](https://guide.freecodecamp.org/git/git-checkout/)

## 删除分支

删除某个分支的命令很简单，使用`git branch -D branchname`即可，但如果我想一次性删除多个分支呢？可以使用`git branch -D $(git branch | grep 3.2*)`，或者"git branch -D `git branch | grep -E '^3\.2\..*'`"。


参考：

- [git branch](https://git-scm.com/docs/git-branch)
- [Can you delete multiple branches in one command with Git?](https://stackoverflow.com/questions/3670355/can-you-delete-multiple-branches-in-one-command-with-git/3670479)

## Q&A

- 新初始化的仓库，提交的时候提示错误

```
error: src refspec main does not match any
error: failed to push some refs to ...
```

在[](https://stackoverflow.com/questions/4181861/message-src-refspec-master-does-not-match-any-when-pushing-commits-in-git)中提到先用`git push origin HEAD:main`可以解决。

# Git使用笔记

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

## 获取更新 / git pull

`git pull` 相当于`git fetch`和`git merge FETCH_HEAD`。

## 常用操作快速索引

- 编辑相关

```
> git checkout
> git add
> git add -u
> git commit
> git commit --amend
> git reset
> git rebase
> git push
```

- 查看相关

```
> git branch -vv
> git status
> git status -s
> git diff
> git show SHA-1
> git show --stat SHA-1
> git config --list
```

- 其他

```
> git branch -m "old_branch_name" "new_branch_name"
```


## 移植修改

要将其他分支的修改移植到本地分支，有三种方法：

- 使用`git cherry-pick`

```
> git cherry-pick SHA-1
> git cherry-pick -n
```

第一条命令会将SHA-1的所有修改移植到当前分支，第二条命令是在移植之前进行选择，可以通过编
辑制定部分修改（*注：待测试。*）

- 使用`git checkout`

```
> git checkout SHA-1 -- "file_name_with_directory"
> git checkout "branch_name" -- "file_name_with_directory"
```

如上两条命令可以将对应分支/版本的某个文件的修改移植到当前分支。

- 用git patch的方式

```
> git format-patch -s SHA-1 # 将SHA-1之后的所有commit都单独生成各自的patch文件。
> git diff SHA-0 SHA-1 > "patch_filename" # 将在SHA-1上的修改生成patch文件。
> git diff "branch_name" -- "file_name_with_directory" > "patch_filename"
> git apply "patch_filename"
```

先在原有分支使用`git diff`生成patch文件，然后在本地分支打patch即可。

- 用patch的方式

```
patch target_file changes.patch
patch < changes.patch
```

如果changes.patch当中存在多层路径，而当前在target_file目录下面，那么可以通过 -p<number>
选项来忽略number层目录，比如：`patch -p1 < changes.patch`忽略1个目录层次多层次时，在
根目录可以直接运用`patch < changes.patch`。

使用`patch -R patched_file changes.patch`来回退补丁。（*注： 待测试。*）


## 设置提交人信息 / config committer

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


## 修改提交人信息 / amend author

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


## 添加远端仓库

在添加远端仓库时不仅支持URL还支持相同服务器的目录寻址，比如：

```
git remote add new_remote_name /home/lianbche/fddmac
git fetch new_remote_name trunk:remotes/new_remote_name/trunk
```

如上的操作分为两步：首先，添加名称为`new_remote_name`的远端仓库，该仓库与目录`/home/lianbche/fddmac
`关联；其次，将远端仓库的`trunk`分支与本地仓库`trunk`关联。


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

## 变基 / git rebase

### onto

将 client 中的修改合并到主分支并发布，但不合并 server 中的修改，因为它们还需要经过更全
面的测试：`$ git rebase --onto master server client`。

```
git rebase --onto 672287559f8c9fc0de5d2c226669ddaf2380240b origin/trunk -i
```

参考：

- [3.6 Git 分支 - 变基](https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%8F%98%E5%9F%BA)


## 取消修改 / undo

我们将“已经生效”分为如下三种情况：一，执行`git add`之后暂存的修改；二，执行`git commit`
之后在本地分支生效的修改；三，执行`git push`已经在远端分支生效的修改。

- 回退`git add`暂存的修改

```
git reset "file or directory"
```

通常来说，已经改动但是没有执行`git add`的文件处于“unstaged”状态，执行`git add`之后便处
于"staged"状态。因此，这里的前一个命令是将"staged"状态的文件回退到"unstaged"状态，处于
“unstaged”状态的文件可以直接通过`git checkout`来还原。

如果是add了新的文件，那么这个时候取消需要执行`git rm -r --cached "file_name"`。

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


## 查阅修改记录 / git blame

使用`git blame -L 160, +10 "filename"`来查看谁修改了代码，-L参数是指定开始行和结束行。
使用`git blame -L10,+1 febdcdfg^ -- "filename"`来blame前一个版本。

## 储藏 / git stash

使用 `git stash`储藏当前修改，用`git stash list`查看所有的储藏，用`git stash apply stasch@{2}`
来指定应用哪一个储藏，如果不指定默认最近的储藏。

## 参考

- [透過rebase -i, reset, revert還原某個commit的方法](http://rubyist.marsz.tw/blog/2012-01-17/git-reset-and-revert-to-rollback-commit/)
- [Git blame — prior commits?](https://stackoverflow.com/questions/5098256/git-blame-prior-commits)

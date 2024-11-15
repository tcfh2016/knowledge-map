## 修改确认：`git add`


如果想在执行`git add`的时候不添加一些文件，那么可以：

- `git add -- . ':!path'`
- 先执行`git add .`，再执行`git reset -- path`回退
- 创建`.gitignore`然后将对应的文件或者路径添加进去

参考：

- [.gitignore File – How to Ignore Files and Folders in Git](https://www.freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git/)


## 修改提交

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

当你发现在当前仓库commit的修改使用了你不想使用的committer信息时，你可以通过三个步骤来修改它。

Step1：使用`git rebase -i SHA1`将修改的commit囊括进来，这里SHA1需要指定你需要修正的那条commit的前一条。

Step2：修改弹出的编辑框内的你需要修改的那条记录前的`pick`为`edit`，保存并退出。

Step3：使用`git commit --amend --author="tcfh2016 <tcfh2016@gmail.com>"`来完成修改。

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

通常来说，已经改动但是没有执行`git add`的文件处于“unstaged”状态，执行`git add`之后便处于"staged"状态。因此，这里的前一个命令是将"staged"状态的文件回退到"unstaged"状态，处于“unstaged”状态的文件可以直接通过`git checkout`来还原。

如果是add了新的文件，那么这个时候取消需要执行`git rm -r --cached "file_name"`。

- 回退本地分支生效的修改

```
git reset SHA-0
git reset --hard SHA-0
```

假设本地修改在`git commit`之后的提交记录为SHA-1，它前一个提交为SHA-0，那么使用前一个命
令可以将SHA-1的修改回退到`unstaged`状态。后一个命令会直接删除SHA-1的修改。

如果要更新具体文件：

```
git reset HEAD -- file_path
git reset HEAD^ -- file_path
git checkout -- file_path
```

- 回退远端分支生效的修改

远端分支已经生效的修改只能通过本地回退，再推送到远端。

方式一：执行`git revert SHA1`在本地回退修改，再执行`git push`推送到远端。

方式二：执行`git rebase -i SHA2`并删除掉SHA1的那次修改（注：SHA2是SHA1的前一个分支），
再执行`git push`推送到远端。

参考：

- [Hard reset of a single file](https://stackoverflow.com/questions/7147270/hard-reset-of-a-single-file)

## 查阅修改 / git diff

1）两个版本之间的修改

先从一个简单的例子开始，比如我们想查看两个版本之前的修改，但是只想查看修改涉及到的文件列表：

```
git diff SHA-OLD SHA-NEW --name-only  # 查看old到new的修改，仅显示文件名称
git diff SHA-OLD SHA-NEW --name-only path_from_curr_directory # 查看old到new的修改，仅显示指定路径的文件名称
```

如果不带有`--name-only`，那么会输出所有的修改内容。然而，如果我们想搜索两个版本之间的commit信息那么需要使用`git log`:*这种方式好像不能对比commit，只能限制时间段*

```
git log SHA-OLD..SHA-NEW --name-only path_from_curr_directory # 查看old到new的提交信息，仅显示指定路径的提交
git log --stat SHA-OLD..SHA-NEW --name-only path_from_curr_directory # 同上，但包括文件的修改
```

另外需要使用`--pretty=format`参数来格式化提交信息：

```
git log --pretty=%H SHA-OLD..SHA-NEW --name-only path_from_curr_directory # 仅显示SHA
git log --pretty=%s SHA-OLD..SHA-NEW --name-only path_from_curr_directory # 仅显示标题
git log --pretty=%h-%ad-%s SHA-OLD..SHA-NEW --name-only path_from_curr_directory # 显示SHA-日期-标题
```

参考：https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%9F%A5%E7%9C%8B%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2#log_options

2）某个commit的修改

```
git show SHA-1 -- path
```

## 查阅修改记录 / git blame

使用`git blame -L 160, +10 "filename"`来查看谁修改了代码，-L参数是指定开始行和结束行。
使用`git blame -L10,+1 febdcdfg^ -- "filename"`来blame前一个版本。

## 储藏 / git stash

使用 `git stash`储藏当前修改，用`git stash list`查看所有的储藏，用`git stash apply stasch@{2}`
来指定应用哪一个储藏，如果不指定默认最近的储藏。

## 参考

- [透過rebase -i, reset, revert還原某個commit的方法](http://rubyist.marsz.tw/blog/2012-01-17/git-reset-and-revert-to-rollback-commit/)
- [Git blame — prior commits?](https://stackoverflow.com/questions/5098256/git-blame-prior-commits)

## 创建`pull request`

1）对于仓库没有写权限

- step1：先`fork`原仓库"A"，得到自己的克隆仓库"clone-A"
- step2：修改本地克隆的仓库
- step3：将修改推送到"clone-A"
- step4: 创建`pull request`
    - 将`pull request`和`issue`关联，自动方式是在request的描述里面使用关键字：`Fixes octo-org/octo-repo#100`

2）对于仓库有写权限

参考：

- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)

## git tag

创建标签有两种形式：轻量级标签和注释标签。

```
git tag v1.4

git tag -a v1.4 -m "my version 1.4"
```

参考：

- [2.6 Git Basics - Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
# Git使用笔记


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
> git show SHA-1:file_name
> git show SHA-1 -- file_name (need whole path)
> git config --list
```

- 其他

```
> git branch -m "old_branch_name" "new_branch_name"
```

## 常见问题

### remove untracked files

本地的git仓库有时候因为编译会产生出一些untracked文件，怎么快速删除这些文件呢？

使用`git clean -f`会移除所在目录下untrack的文件，但不包括目录，可以先用`git clean -n`查看哪些文件会被移除。

### Filename too long

在切换分支的时候提示下面错误，原因在于Windows下面对文件名的长度有限制，配置`git config core.longpaths true`之后即可。

```
error: cannot stat 'cplane/cu/cp_ue...and_PLMN_MP_at_HO.parameters': Filename too long
```

参考：

- [git pull aborted with error filename too long](https://stackoverflow.com/questions/21123415/git-pull-aborted-with-error-filename-too-long/22831095)

### fatal: bad config line 1 in file C:/Users/lianbche/.gitconfig

早上电脑没电关机，之后重启后发现不管执行什么git命令都会提示`fatal: bad config line 1 in file C:/Users/lianbche/.gitconfig`，之后在[Bad git config file .git/config](https://stackoverflow.com/questions/9509125/bad-git-config-file-git-config)查找到解决方法。

很简单，就是将任一仓库下面的`.git\config`拷贝到提示.gitconfig无效的目录并重命名替换它即可。

###

https://jasonkayzk.github.io/2019/10/10/%E5%85%B3%E4%BA%8E%E4%BD%BF%E7%94%A8Git%E6%97%B6push-pull%E8%B6%85%E6%97%B6-%E4%BB%A5%E5%8F%8AGithub%E8%AE%BF%E9%97%AE%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95/

https://segmentfault.com/a/1190000037797501

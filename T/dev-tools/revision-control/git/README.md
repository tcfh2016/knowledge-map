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

### fatal: bad config line 1 in file C:/Users/lianbche/.gitconfig

早上电脑没电关机，之后重启后发现不管执行什么git命令都会提示`fatal: bad config line 1 in file C:/Users/lianbche/.gitconfig`，之后在[Bad git config file .git/config](https://stackoverflow.com/questions/9509125/bad-git-config-file-git-config)查找到解决方法。

很简单，就是将任一仓库下面的`.git\config`拷贝到提示.gitconfig无效的目录并重命名替换它即可。

## 安装 

不同的linux版本可能使用不同的命令：

```
yum install git
```

参考：

- [PIP Install Git – A Quick Read](https://www.activestate.com/resources/quick-reads/pip-install-git/)

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

## SSH

首先执行`ssh-keygen -t ed25519 -C "your_email@example.com"`生成新的SSH key。

然后将上面的SSH key添加到ssh-agent，先用`eval "$(ssh-agent -s)"`将ssh-agent启动起来，再使用`ssh-add ~/.ssh/id_ed25519`将SSH Key添加到ssh-agent。

然后将`cat ~/.ssh/id_ed25519.pub`得到的公钥内容添加到github上。

参考：

- [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
- [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux)


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

### fatal: index file corrupt

昨天在git add之后电脑没有电关机了，今天重新开机执行`git status`命令出现了如下错误：

```
PS> git status -s
error: bad signature
fatal: index file corrupt
```

解决方法，是先删除`.git\index`，然后`git reset`即可。

参考：

- [How to resolve "Error: bad index – Fatal: index file corrupt" when using Git](https://stackoverflow.com/questions/1115854/how-to-resolve-error-bad-index-fatal-index-file-corrupt-when-using-git)

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



### fatal: your current branch appears to be broken

有次电脑没电关机，之后开机发现git无法正常使用，执行`git log`提示“fatal: your current branch appears to be broken”的错误。

解决方法为：

```
1 get backup from your .git directory
2 open file .git\logs\refs\heads\<branch name> with your editor 
3 copy second hash of your last line
4 open file .git\refs\heads\<branch name> and delete everything in this file
5 past that hash to .git\refs\heads\<branch name>
```

参考：

- [fatal: your current branch appears to be broken](https://stackoverflow.com/questions/57580891/fatal-your-current-branch-appears-to-be-broken)


### `Bad server host key: Invalid key length `

突然在服务器上无法更新git仓库，总是提示下面这个错误：

```
Bad server host key: Invalid key length 
fatal: Could not read from remote repository.
```

解决方案是将`~/.ssh/known_hosts`里面有关gerrit地址删除，重新更新。
# 命令与PATH

在我们在命令行键入命令时，系统并不会搜索所有目录去找到该命令对应的可执行文件，因为耗时太大。所以系统维护了一个路径的集合，这个集合被定义在`PATH`里面。

```
# 打印出当前的PATH，是包含了以冒号“:”作为分隔符的多个路径
echo $PATH

# 将自己需要的路径（“my_own_path”）设置到PATH里面
export PATH=$PATH:my_own_path
```

# 常用命令

## `source`

`source`命令用来在当前shell里面（当前进程）执行该脚本，不同于使用`sh script.sh`会在新的子进程里面执行脚本的方式。

参考：

- [利用 source 來執行腳本：在父程序中執行](http://linux.vbird.org/linux_basic/0340bashshell-scripts.php#some_ex_run)


## 常见命令

- `export`是告诉shell让后面的命令对该shell所有子进程生效。
- `alias name=value`给长的命令创建短的别名，比如`alias l='ls -l'`。
- `w -h`查看登入用户的信息


## 静态库符号查看

```
nm libStubs.a | grep -i "TestInitiationReq" 
```

## netstat

`netstat`可以查询目前主机打开的网络服务端口。比如使用`netstat -tuln`可以取得目前主机启动的服务。

常见的端口信息：

- 80: www
- 22: ssh
- 21: ftp
- 25: mail
- 111: RPC
- 631: CUPS

## 查看：`ls`

1) 查看文件大小，以“MB”单位显示

执行`ll`默认的单位为字节，但使用`ls -l --block-size=M`可以按照兆字节展示，换算单位为：1MB = 1024 * 1024 B。

或者执行`ls -lh`以便于阅读的方式展示出来。


参考：

- [How do I make `ls` show file sizes in megabytes?](https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes)


2) 按修改顺序显示

使用`ls -lr --sort=time`可以按照时间倒数排序。`-r`是倒叙显示，`-l`是长列表显示。

```
--sort=WORD
sort by WORD instead of name: none (-U), size (-S), time (-t), version (-v), extension (-X)
```

# 参考

- [10 Essential Terminal Commands Every Developer Should Know](https://www.trevorlasn.com/blog/10-essential-terminal-commands-every-developer-should-know)


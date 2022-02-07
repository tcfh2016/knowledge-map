## 常用命令

## 搜索命令

在特定目录下搜索文本中的关键字，使用`grep -rnw '/path/to/somewhere/' -e 'pattern'`，其中的`-r`代表递归搜索，`-n`代表显示行号，`-w`表示全字匹配。


参考：

- [How do I find all files containing specific text on Linux?](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)

## 查看文件

如何使用`ll`按照时间排序？

```
按大小排序
[root@localhost ~]# ll -Sh

按时间排序，带-r是反序
[root@localhost ~]# ll -rt
```

## 磁盘空间

`df`（全称`disk free`）命令用来查看磁盘空间的整体情况，比如各个disk drive分区占用了多少。

```
查看磁盘状态，-h表示以human-readable的格式显示
df -lh

查看特定文件系统的磁盘使用情况
df -lh
```

`du`（全称`disk usage`）命令用来展示文件系统的空间使用，默认递归显示当前目录下所有文件和文件夹的空间信息。

```
查看当前文件夹下所有文件大小（包括子文件夹）, -s表示当前目录的总体情况，-h表示易读的格式。
du -hs

查看制定文件夹大小。
du -hs ftp

统计当前目录下所有文件、文件夹大小。
du -h --max-depth=1
```

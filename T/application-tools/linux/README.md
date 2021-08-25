## 常用命令

## 查看文件

如何使用`ll`按照时间排序？

```
按大小排序
[root@localhost ~]# ll -Sh

按时间排序，带-r是反序
[root@localhost ~]# ll -rt
```

## 磁盘空间

```
查看当前文件夹下所有文件大小（包括子文件夹）。
du -h
查看制定文件夹下所有文件大小（包括子文件夹）。
du -h ftp
查看制定文件夹大小。
du -hs ftp

统计文件夹大小：
du -h --max-depth=1
```

## 磁盘空间

## df

`df`（全称`disk free`）命令用来查看磁盘空间的整体情况，比如各个disk drive分区占用了多少。

```
查看磁盘状态，-h表示以human-readable的格式显示
df -lh

查看特定文件系统的磁盘使用情况
df -lh
```

## du

`du`（全称`disk usage`）命令用来展示文件系统的空间使用，默认递归显示当前目录下所有文件和文件夹的空间信息。

```
# 查看指定文件夹下所有文件大小（包括子文件夹）, -s表示当前目录的总体情况，-h表示易读的格式。
du -hs ftp

# 统计当前目录下所有文件、文件夹大小。
du -h --max-depth=1

# 统计home目录下各用户占用空间，并排序
du -s /home/* | sort -nr
```

在使用`du`命令进行磁盘统计的时候可能因为权限问题收到很多“”的打印，参考[Exclude all permission denied messages from "du"](https://stackoverflow.com/questions/15141588/exclude-all-permission-denied-messages-from-du)来解决。方法：

```
du -cBM --max-depth=1 2>&1 | grep -v 'denied' | sort -n 
```


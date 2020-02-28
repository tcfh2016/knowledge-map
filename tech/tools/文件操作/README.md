## 搜索文件

```
# 指定当前目录的搜索深度。
find . -maxdepth 3 -name "*core"

#搜索当前目录所有以my开头的文件名，并显示详细信息。
find . -name 'my*' -ls

#搜索用户目录下所有以m开头的文件，相比find它查找目录数据库 /var/lib/locatedb。
locate ~/m

#所搜grep，仅搜索程序名。
whereis grep

#在PATH指定的路径中搜索。
which grep
```

参考：

- [Linux的五个查找命令](http://www.ruanyifeng.com/blog/2009/10/5_ways_to_search_for_files_using_the_terminal.html)


## 查看文件被什么进程占用

```
fuser file_name
/sbin/fuser file_name
```

## 查看目录结构

```
tree /F # Windows下打印目录结构
```


## 参考

- [List of Command Prompt Commands](https://www.lifewire.com/list-of-command-prompt-commands-4092302)

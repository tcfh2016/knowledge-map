
## 设定确定的目录

有些常用的目录会反复跳转，如何设定快捷键类似的功能？

可以在.bashrc里面设定变量，然后在切换目录的时候使用变量就可以了。记得修改完之后需要重新
执行一遍.bashrc让它生效。

参考：

- [第十一章、认识与学习 BASH](http://cn.linux.vbird.org/linux_basic/0320bash.php#alias_history)

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

查找的时候如果排除特定文件夹：

```
find . -path ./misc -prune -o -name '*.txt' -print
find . -type d \( -path dir1 -o -path dir2 -o -path dir3 \) -prune -o -print
find -name "*.js" -not -path "./directory/*"
```

find . -name "*.txt" | xargs grep -i "text_pattern"




参考：

- [Linux的五个查找命令](http://www.ruanyifeng.com/blog/2009/10/5_ways_to_search_for_files_using_the_terminal.html)


## Windows 下面的zip包里面搜索文件

使用`7z l compressed.tar namefile -r`似乎只能够找到压缩包里面目录包含的文件，但是没有办法查找zip里面的zip文件。



参考：

- [How do I search the content of 7-Zip archives (.7z)?](https://superuser.com/questions/326737/how-do-i-search-the-content-of-7-zip-archives-7z)


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

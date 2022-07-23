
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


## 搜索命令

在特定目录下搜索文本中的关键字，使用`grep -rnw '/path/to/somewhere/' -e 'pattern'`，其中的`-r`代表递归搜索，`-n`代表显示行号，`-w`表示全字匹配。


参考：

- [How do I find all files containing specific text on Linux?](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)


```
# 搜索文件夹下.hpp包含"getRise()"的文件，并打印行号（-n）

find directory/ -name "*.hpp"|xargs grep -n getRise()

-path ./uplane/sdkuplane -prune -o

```

find directory/ -name "CCSEarlyConfig.xml"|xargs grep -n "<tag name="ccs.service.aamem.hpdmpool.id" type="u32">26</tag>"

<tag name="ccs.service.aamem.hpdmpool.id" type="u32">26</tag>

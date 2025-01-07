## 查找程序

#搜索用户目录下所有以m开头的文件，相比find它查找目录数据库 /var/lib/locatedb。
locate ~/m

#所搜grep，仅搜索程序名。
whereis grep

#在PATH指定的路径中搜索。
which grep


## 搜索文件：`find`

```
# 指定当前目录的搜索深度。
find . -maxdepth 3 -name "*core"

# 搜索当前目录所有以my开头的文件名，并显示详细信息。
find . -name 'my*' -ls
find -name "*.js" -not -path "./directory/*"

# 排除特定文件夹：
find . -path ./misc -prune -o -name '*.txt' -print
find . -type d \( -path dir1 -o -path dir2 -o -path dir3 \) -prune -o -print
```


参考：

- [Linux的五个查找命令](http://www.ruanyifeng.com/blog/2009/10/5_ways_to_search_for_files_using_the_terminal.html)


## 搜索命令：`grep`

使用方式：

```
# 搜索文件内容 
grep "find something" file.txt

# '-i'忽略大小写，'-c'打印匹配次数
grep -i -c "find something" file.txt

# 多次使用'-e'去匹配多个条件
grep -e "error" -e "404" system.log

# '-o'近打印匹配的内容，'-r'进行文件夹内递归搜索
grep -o -r "something" directory | wc -l

# `-r`代表递归搜索，`-n`代表显示行号，`-w`表示全字匹配
grep -rnw '/path/to/somewhere/' -e 'pattern'
```


参考：

- [How do I find all files containing specific text on Linux?](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)
- [10 Essential Terminal Commands Every Developer Should Know](https://www.trevorlasn.com/blog/10-essential-terminal-commands-every-developer-should-know)


## `find`结合`grep`

```
find . -name "*.txt" | xargs grep -i "text_pattern"
find . -name "*.*pp" -not -path "*/tst/*" | xargs grep  "em_.*("
```

举例：搜索文件夹下.hpp包含"getRise()"的文件，并打印行号（-n）

find directory/ -name "CCSEarlyConfig.xml"|xargs grep -n "aamem.hpdmpool.id"

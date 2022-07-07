
## 查看文件

如何使用`ll`按照时间排序？

```
按大小排序
[root@localhost ~]# ll -Sh

按时间排序，带-r是反序
[root@localhost ~]# ll -rt
```


## 搜索命令

在特定目录下搜索文本中的关键字，使用`grep -rnw '/path/to/somewhere/' -e 'pattern'`，其中的`-r`代表递归搜索，`-n`代表显示行号，`-w`表示全字匹配。


参考：

- [How do I find all files containing specific text on Linux?](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)


## 搜索

- [文本搜索 / grep](./grep.md)

## 统计

- [统计/wc](./wc.md)

## 操纵

- [行处理/sed](./sed.md)
- [列处理/awk](./awk.md)
- [切分/split](./split.md)

```
# 搜索文件夹下.hpp包含"getRise()"的文件，并打印行号（-n）

find directory/ -name "*.hpp"|xargs grep -n getRise()

-path ./uplane/sdkuplane -prune -o

```

find directory/ -name "CCSEarlyConfig.xml"|xargs grep -n "<tag name="ccs.service.aamem.hpdmpool.id" type="u32">26</tag>"

<tag name="ccs.service.aamem.hpdmpool.id" type="u32">26</tag>

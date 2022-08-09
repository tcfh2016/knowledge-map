## 查看文件格式

```
[lianb]$ file delete_all.sh
delete_all.sh: Bourne-Again shell script, ASCII text executable
```
如果是Windows下的文件，后面会带有`with CRLF line terminators`。之后就可以使用`dos2unix`或者`unix2dos`来进行格式的转换了。

## 清空文件

对于`/var`目录的一些文件无法删除，比如这个目录下面有账户对应的`/var/spool/mail/lianb`，没用办法使用`rm`去删除，但可以使用`> /var/spool/mail/lianb`将其清空。

## 设定确定的目录

有些常用的目录会反复跳转，如何设定快捷键类似的功能？

可以在.bashrc里面设定变量，然后在切换目录的时候使用变量就可以了。记得修改完之后需要重新
执行一遍.bashrc让它生效。

参考：

- [第十一章、认识与学习 BASH](http://cn.linux.vbird.org/linux_basic/0320bash.php#alias_history)


## 查看文件被什么进程占用

```
fuser file_name
/sbin/fuser file_name
```

## 查看文件

如何使用`ll`按照时间排序？

```
按大小排序
[root@localhost ~]# ll -Sh

按时间排序，带-r是反序
[root@localhost ~]# ll -rt
```

## 统计/wc

统计文件的行数。

```
wc -l file_name  # 统计file_name的行数。
ls -a | wc -l    # 灵活用法：查看目录a中的文件个数。
```
参数：

- -c, --bytes: print the byte counts
- -m, --chars: print the character counts
- -l, --lines: print the newline counts
- -w, --words: print the word counts      

## 切分/split

切分文件。

```
split -b 15m error.log         # 以15M的大小分隔，生成文件名xaa,xab
split -b 15 error.log mylog -d # 以15字节大小分隔，生成文件名mylog01, mylog02
cat xaa  xab > large.log       # 还原分隔的文件
```

参数：

- -b, --bytes=SIZE: put SIZE bytes per output file      
- -l, --lines=NUMBER: put NUMBER lines per output file
- -d, --numeric-suffixes: use numeric suffixes instead of alphabetic

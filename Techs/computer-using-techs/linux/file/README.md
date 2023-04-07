## 文件类型

可以通过`test`命令来判断文件的类型，注意`test`的更方便的写法是`[ -d file]`这样子。

-d file: True if file is a directory.
-e file: True if file exists.
-f file: True if file exists and is a regular file.

```

find ./ -type d
find ./ -type f
```

参考：

- [](https://stackoverflow.com/questions/747465/recursively-list-all-directories-and-files)


## 判断内容是否存在

```
#!bin/sh

if ! [ -f test.txt ] ;then   # if [ ! -f test.txt ]
    echo "file.txt exist"
else
    echo "file.txt not exist"
fi
```

## 读出文件内容

使用和shell命令行下同样的命令：

```
#!bin/sh

# 读取整个文件内容
cat filename

# 读取文件第一行
head -n 1 filename 

# 循环读取文件内容，每次读第一行
while read line; do
    echo "$line"
done < file.txt
```

如果要将读取的内容赋值到变量，就如下使用：*注意，=左右两边不能有空格。*

```
first_line=`head -n 1 filename`
echo $first_line
```


参考：

- [How to get the first line of a file in a bash script?](https://stackoverflow.com/questions/2439579/how-to-get-the-first-line-of-a-file-in-a-bash-script)
- [The read builtin command](https://wiki.bash-hackers.org/commands/builtin/read)


## 遍历子目录

一个最简单的版本是遍历某个目录的内容，然后分别处理。比如我只想处理某个目录下面的所有第一层子目录：

```
work_dir="~/$USER/logs"
dirs=$(ls ${work_dir})

IFS=' ' read -ra ADDR <<< ${dirs}
for e in "${ADDR[@]}"; do
  if [ -d ${e} ]; then
    echo "${e}"
  fi
done
```

但这并不是推荐做法，两个原因：

1. 是对于目录的名称可以用除了`/`之外的字符来命名，这使得对`find`或者`ls`命令的输出内容将很难解析。比如如上代码使用空格` `来作为分隔符，但如果恰好其中一个子目录名称包含了空格就不好办了。比如在[Why does my shell script choke on whitespace or other special characters?](https://unix.stackexchange.com/questions/131766/why-does-my-shell-script-choke-on-whitespace-or-other-special-characters)提到的问题。

2. 读取文件性能太低。这个在[](https://unix.stackexchange.com/questions/169716/why-is-using-a-shell-loop-to-process-text-considered-bad-practice)里面有个很好的比喻，每一次调用命令都是耗时的，执行一次命令可能调用由“数千行C语言”编写的程序，涉及到资源准备、操作和清理等工作。同时，不同命令的执行都是以单独进程形式进行，所以按行进行读取并操作是费时的。


参考：

- [Why is using a shell loop to process text considered bad practice?](https://unix.stackexchange.com/questions/169716/why-is-using-a-shell-loop-to-process-text-considered-bad-practice)
- [Applying bash operations to first level subfolders of a folder](https://unix.stackexchange.com/questions/497887/applying-bash-operations-to-first-level-subfolders-of-a-folder)
- [Why is looping over find's output bad practice?](https://unix.stackexchange.com/questions/321697/why-is-looping-over-finds-output-bad-practice)

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

## 创建文件

`touch`可以创建文件，但是不能创建目录。


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

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
## shell脚本里面读出文件内容

使用和shell命令行下同样的命令：

```
#!bin/sh

cat filename #读取整个文件内容
head -n 1 filename #读取文件第一行
```

如果要将读取的内容赋值到变量，就如下使用：*注意，=左右两边不能有空格。*

```
first_line=`head -n 1 filename`
echo $first_line
```


参考：

- [How to get the first line of a file in a bash script?](https://stackoverflow.com/questions/2439579/how-to-get-the-first-line-of-a-file-in-a-bash-script)


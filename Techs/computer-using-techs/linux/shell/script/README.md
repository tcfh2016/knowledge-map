## [Shell Script](https://www.shellscript.sh/)

## if...else...

```
if [ ... ]
then
  # if-code
else
  # else-code
fi
```

## for 循环

[Shell script "for" loop syntax](https://stackoverflow.com/questions/1445452/shell-script-for-loop-syntax)：

```
max=10
for (( i=2; i <= $max; ++i ))
do
    echo "$i"
done
```

## 注释

单行用`#`，多行用`''`。参考[Way to create multiline comments in Bash?](https://stackoverflow.com/questions/43158140/way-to-create-multiline-comments-in-bash)。

## 字符串匹配

参考How to check if a string contains a substring in Bash](https://stackoverflow.com/questions/229551/how-to-check-if-a-string-contains-a-substring-in-bash)：

```
string='My long string'
if [[ $string == *"My long"* ]]; then
  echo "It's there!"
fi
```

## 字符串切片

在[这里](https://blog.csdn.net/rockstics/article/details/116917653)有一篇有关字符串切片的文章：

```
str=abced
echo ${#str} #5

${var:offset} #取offset -> length-1的字符串
${var: -length} #-length -> length-1的字符串，冒号后必须有空格
echo ${#str:1} #bced
echo ${#str: -2} #ed

${var:offset:-length} #取从offset开始，到倒数length字符之间的字符串，去掉头尾
echo ${#str:0:-1} #abce
```

或参考[Shell脚本编程之字符串切片](https://www.cnblogs.com/haona_li/p/10334057.html)。

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

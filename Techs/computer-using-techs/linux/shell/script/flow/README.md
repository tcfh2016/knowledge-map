## if语句

shell里面每个命令执行之后都会返回一个状态（退出状态），这是一个整数，通常0代表执行成功。可以通过打印`$?`来查看上一次的执行结果。

```
if command
then
  # if-code
else
  # else-code
fi

if command; then
  # if-code
elif command; then
  # elif-code
else
  # else-code
fi
```


## test命令

test命令通常和if语句结合起来判断结果为true/false的命令，它有两种形式：`test expression`和`[ expression ]`。

test命令是shell内建命令，可以通过`help test`来查看，常用的包括：

- -d file: True if file is a directory.
- -e file: True if file exists.
- -f file: True if file exists and is a regular file.
- -L file: True if file is a symbolic link.
- -z string: True if string is empty.
- -n string: True if string is not empty.
- string1 = string2: True if string1 equals string2.
- string1 != string2: True if string1 does not equal string2.


## for 循环

[Shell script "for" loop syntax](https://stackoverflow.com/questions/1445452/shell-script-for-loop-syntax)：

```
max=10
for (( i=2; i <= $max; ++i ))
do
    echo "$i"
done
```
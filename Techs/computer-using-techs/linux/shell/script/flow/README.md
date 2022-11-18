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

*上面代码语句的缩进在shell里面并不是必须的，只是为了可读性才如此做。*


## test命令

test命令通常和if语句结合起来判断结果为true/false的命令，它有两种形式：`test expression`和`[ expression ]`。常见的是后面这种形式，但对于初学者而言没有这些信息便会摸不着头脑。

test命令是shell内建命令，可以通过`help test`来查看，常用的包括：

- -d file: True if file is a directory.
- -e file: True if file exists.
- -f file: True if file exists and is a regular file.
- -L file: True if file is a symbolic link.
- -z string: True if string is empty.
- -n string: True if string is not empty.
- string1 = string2: True if string1 equals string2.
- string1 != string2: True if string1 does not equal string2.


## case

类似于C语言中的`switch...case...`语句：

```
case word in
    patterns ) commands ;;
esac
```


## while 循环

```
number=0
while [ "$number" -lt 10 ]; do
    echo "Number = $number"
    number=$((number + 1))
done

number=0
until [ "$number" -ge 10 ]; do
    echo "Number = $number"
    number=$((number + 1))
done
```


## for 循环

[Shell script "for" loop syntax](https://stackoverflow.com/questions/1445452/shell-script-for-loop-syntax)：

基本的格式为：

```
for variable in words; do
    commands
done
```

其中的words可以是`word1 word2 word3`，也可以是`$(cat ~/.bash_profile)`这样的单词集合。


```
max=10
for (( i=2; i <= $max; ++i ))
do
    echo "$i"
done
```
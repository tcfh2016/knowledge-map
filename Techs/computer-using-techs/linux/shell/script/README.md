## Shell Script

Shell脚本，可以简单的理解为“包含一系列命令的文件”，执行它就类似于通过命令行执行多条命令。所以，shell脚本有利于我们将一些事情自动化。

以下是一些基本的使用知识，便于快速入门：

1）使用`var=value`的形式创建变量，*特别注意等号两边不能有空格*。然后使用`$var`来引用变量，推荐做法是引用变量的时候都加上双括号：`"$foo"`，原因是因为`$var`本身的并不仅仅是引用原有变量的值，而且会把它按照空格拆分为对应的列表，比如`var="hello world"`，使用`$var`拿到的是“hello”和“world”两个单词的列表。

比如你用`[ -d $dir ]`判断dir是不是目录，使用`$dir`就会提示“too many arguments”，正确的方法是使用`"$dir"`。


参考：

- [Why does my shell script choke on whitespace or other special characters?](https://unix.stackexchange.com/questions/131766/why-does-my-shell-script-choke-on-whitespace-or-other-special-characters)


2）使用替代命令：`$(expression)`，比如`$(date +"%x %r %Z")`会执行`date +"%x %r %Z"`命令。另一种相对较老的版本是用\`expression\`，它和`%(expression)`是等价的，但是老版本不具备良好的可移植性。

参考：

- [Why does my shell script choke on whitespace or other special characters?](https://unix.stackexchange.com/questions/131766/why-does-my-shell-script-choke-on-whitespace-or-other-special-characters)

3）使用`$((expression))`可以进行数值计算。

- 在shell脚本中，进行算术计算需要特定的算数表达式：`$((oper1 + oper2))`，支持`+ - * / %`。

4）使用分号`;`可以将多行代码连接在一行。
5）如果一行代码内容太多，可以使用`\回车`来扩展至下一行。

## 好的实践

- 编写表达式的时候可以使用双引号将表达式括起来，避免因为空格导致语法错误。比如`[ $number = "1" ]`可能因为变量number因为没有设置而出现语法错误。
- 在脚本结束时使用`exit`来执行退出并设置退出状态，如`exit 0`，`exit 1`。


参考：

- [Writing Shell Scripts](https://linuxcommand.org/lc3_writing_shell_scripts.php)
- [Way to create multiline comments in Bash?](https://stackoverflow.com/questions/43158140/way-to-create-multiline-comments-in-bash)。
- [Why does my shell script choke on whitespace or other special characters?](https://unix.stackexchange.com/questions/131766/why-does-my-shell-script-choke-on-whitespace-or-other-special-characters)

## 变量的使用

常用变量：

- $USER
- $HOME


引用变量时使用`${var}`相比`$var`的好处：正常情况下，使用`$var`来引用变量是可以的，但有些时候这样行不通。情况下：假设`caseid`是一个变量，要根据变量拼接文件路径

- 使用`$caseid_L2STATS.csv`就会有歧义，应该使用"${caseid}_L2STATS.csv"。
- 同样的使用`cat f | grep -e "$casename_[0-9]\+_[0-9]\+"`来查找对应的行信息也不行，比如使用`cat f | grep -e "${casename}_[0-9]\+_[0-9]\+"`。


## 执行shell脚本

shell脚本的执行方式分为两种，第一种为采用绝对路径或者相对路径的执行方式；另一种是使用`source`命令。两种区别如下：

- 采用绝对路径或者相对路径执行脚本的时候，该脚本是在当前进程新建了一个“子进程”来执行脚本，因此脚本在子进程中执行涉及的数据对于当前进程是不可见的。
- 而采用`source`命令来执行时，是直接在当前进程中执行。

这也是为什么我们修改了`~/.bashrc`等配置文件时，如果想让它立即生效那么就会键入`source ~/.bashrc`。

执行之前可以先对脚本进行预检，语法格式为`sh [-nvx] scripts.sh`：

- -n 不执行脚本，仅检查语法问题
- -v 在执行script前，先将脚本内容显示到屏幕上
- -x 将使用到的脚本内容显示到屏幕上

## export $DISPLAY

参考：

- []()

## 注释

单行使用`#`，多行可以使用：

- `<<Block_comment`/`Block_comment`。
- 或者`:'`开始，`'`结束，但这种多行注释方式并不推荐。


参考：

- [Shell Comments](https://bash.cyberciti.biz/guide/Shell_Comments)
- [Writing Comments in Bash Scripts: Single Line, Inline and Multi-line Comments](https://linuxhandbook.com/comments-bash-script/)




## 计时

两种方式。第一种：使用DATE

```
START=$(date +%s)
...
END=$(date +%s)

DIFF=$(( $END - $START ))
echo "It took $DIFF seconds"
```


第二种：使用`SECONDS`变量

```
start=$SECONDS
...
duration=$(( SECONDS - start ))

echo "This run took $duration seconds"
```

参考：

- [](https://stackoverflow.com/questions/385408/get-program-execution-time-in-the-shell)

## `syntax error: unexpected end of file`

出现该问题通常和两种情况有关：一、格式问题，比如Windows下面编写的文件拿到Linux下面执行，因为行末的字符不一样；二、条件语句不匹配问题。

情况一可以通过`file`命令来查看文件格式；情况二需要仔细检查`if...fi`, `for...done`是否匹配。

参考：

- [Bash syntax error: unexpected end of file](https://stackoverflow.com/questions/6366530/bash-syntax-error-unexpected-end-of-file)
- [Bash script: Unexpected end of file error](https://linuxconfig.org/bash-script-unexpected-end-of-file-error)
- [【shell】真正解决syntax error:unexpected end of file？](https://www.cnblogs.com/jessepeng/p/12202626.html)


## 使用字典

```
declare -A sounds
sounds[dog]="Bark"
sounds[wolf]="Howl"
```

参考：

- [Is there a way to create key-value pairs in Bash script?](https://stackoverflow.com/questions/14370133/is-there-a-way-to-create-key-value-pairs-in-bash-script)
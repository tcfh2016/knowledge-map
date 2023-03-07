## Shell Script

Shell脚本，可以简单的理解为“包含一系列命令的文件”，执行它就类似于通过命令行执行多条命令。所以，shell脚本有利于我们将一些事情自动化。


单行用`#`。多行用`:'`开始，`'`结束，但这种多行注释方式并不推荐。

- 使用`var=value`的形式创建变量，*特别注意等号两边不能有空格*。然后使用`$var`来引用变量。
- 使用替代命令：`$(expression)`，比如`$(date +"%x %r %Z")`会执行`date +"%x %r %Z"`命令。另一种相对较老的版本是用"`expression`"，它和"%(expression)"是等价的。而使用`$((expression))`可以进行数值计算。
- 使用分号`;`可以将多行代码连接在一行。
- 如果一行代码内容太多，可以使用`\回车`来扩展至下一行。
- 在shell脚本中，进行算术计算需要特定的算数表达式：`$((oper1 + oper2))`，支持`+ - * / %`。
- good实践：
    - 编写表达式的时候可以使用双引号将表达式括起来，避免因为空格导致语法错误。比如`[ $number = "1" ]`可能因为变量number因为没有设置而出现语法错误。
    - 在脚本结束时使用`exit`来执行退出并设置退出状态，如`exit 0`，`exit 1`。


参考：

- [Writing Shell Scripts](https://linuxcommand.org/lc3_writing_shell_scripts.php)
- [Way to create multiline comments in Bash?](https://stackoverflow.com/questions/43158140/way-to-create-multiline-comments-in-bash)。


## 执行方式

shell脚本的执行方式分为两种，第一种为采用绝对路径或者相对路径的执行方式；另一种是使用`source`命令。两种区别如下：

- 采用绝对路径或者相对路径执行脚本的时候，该脚本是在当前进程新建了一个“子进程”来执行脚本，因此脚本在子进程中执行涉及的数据对于当前进程是不可见的。
- 而采用`source`命令来执行时，是直接在当前进程中执行。

这也是为什么我们修改了`~/.bashrc`等配置文件时，如果想让它立即生效那么就会键入`source ~/.bashrc`。

执行之前可以先对脚本进行预检，语法格式为`sh [-nvx] scripts.sh`：

- -n 不执行脚本，仅检查语法问题
- -v 在执行script前，先将脚本内容显示到屏幕上
- -x 将使用到的脚本内容显示到屏幕上


## 注释

单行使用`#`，多行使用`<<Block_comment`/`Block_comment`。

参考：

- [Shell Comments](https://bash.cyberciti.biz/guide/Shell_Comments)
- [Writing Comments in Bash Scripts: Single Line, Inline and Multi-line Comments](https://linuxhandbook.com/comments-bash-script/)


## 常用变量

- $USER
- $HOME



## `syntax error: unexpected end of file`

出现该问题通常和两种情况有关：一、格式问题，比如Windows下面编写的文件拿到Linux下面执行，因为行末的字符不一样；二、条件语句不匹配问题。

情况一可以通过`file`命令来查看文件格式；情况二需要仔细检查`if...fi`, `for...done`是否匹配。

参考：

- [Bash syntax error: unexpected end of file](https://stackoverflow.com/questions/6366530/bash-syntax-error-unexpected-end-of-file)
- [Bash script: Unexpected end of file error](https://linuxconfig.org/bash-script-unexpected-end-of-file-error)
- [【shell】真正解决syntax error:unexpected end of file？](https://www.cnblogs.com/jessepeng/p/12202626.html)

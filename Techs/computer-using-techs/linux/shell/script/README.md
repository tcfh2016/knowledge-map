## [Shell Script](https://www.shellscript.sh/)

Shell脚本，可以简单的理解为“包含一系列命令的文件”，执行它就类似于通过命令行执行多条命令。所以，shell脚本有利于我们将一些事情自动化。


单行用`#`。多行用`:'`开始，`'`结束，但这种多行注释方式并不推荐。


参考：

- [Writing Shell Scripts](https://linuxcommand.org/lc3_writing_shell_scripts.php)
- [Way to create multiline comments in Bash?](https://stackoverflow.com/questions/43158140/way-to-create-multiline-comments-in-bash)。



## 常见问题

## `syntax error: unexpected end of file`

出现该问题通常和两种情况有关：一、格式问题，比如Windows下面编写的文件拿到Linux下面执行，因为行末的字符不一样；二、条件语句不匹配问题。

情况一可以通过`file`命令来查看文件格式；情况二需要仔细检查`if...fi`, `for...done`是否匹配。

参考：

- [Bash syntax error: unexpected end of file](https://stackoverflow.com/questions/6366530/bash-syntax-error-unexpected-end-of-file)
- [Bash script: Unexpected end of file error](https://linuxconfig.org/bash-script-unexpected-end-of-file-error)
- [【shell】真正解决syntax error:unexpected end of file？](https://www.cnblogs.com/jessepeng/p/12202626.html)

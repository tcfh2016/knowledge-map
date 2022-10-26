## 常见问题

## `syntax error: unexpected end of file`

出现该问题通常和两种情况有关：一、格式问题，比如Windows下面编写的文件拿到Linux下面执行，因为行末的字符不一样；二、条件语句不匹配问题。

情况一可以通过`file`命令来查看文件格式；情况二需要仔细检查`if...fi`, `for...done`是否匹配。

参考：

- [Bash syntax error: unexpected end of file](https://stackoverflow.com/questions/6366530/bash-syntax-error-unexpected-end-of-file)
- [Bash script: Unexpected end of file error](https://linuxconfig.org/bash-script-unexpected-end-of-file-error)
- [【shell】真正解决syntax error:unexpected end of file？](https://www.cnblogs.com/jessepeng/p/12202626.html)

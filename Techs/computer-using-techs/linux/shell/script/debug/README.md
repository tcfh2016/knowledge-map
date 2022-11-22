## 调试

## 注释

注释部分，然后使用`echo`打印出关键信息。那如何通过`echo`打印空格或者tab ？

可以使用`echo -e ' \t '`，这里的-e参数表示使能反斜杠的解析。

- [Echo tab characters in bash script](https://stackoverflow.com/questions/525872/echo-tab-characters-in-bash-script)


## tracing

在脚本的首行，将`#!bin/bash`改为`#!bin/bash -x`，这样脚本在执行的时候会显示每行。


参考：

- [Stay Out of Trouble](https://linuxcommand.org/lc3_wss0090.php)


## [程序管理](http://linux.vbird.org/linux_basic/0440processcontrol.php)

##

1) 如何一次性kill多个进程？

使用`kill -9 pid`可以杀掉单个进程，传入多个pid可以一次性结束多个进程，所以使用这种方式我们需要先将相关进程的pid找到，比如：

> kill -9 `ps -ef | grep oraxpo | grep -v grep | awk '{print $2}'`

另一种方式是使用`pkill httpd`来结束所有与`httpd`相关的所有进程。

参考：

- [How to kill multiple processes](https://unix.stackexchange.com/questions/296086/how-to-kill-multiple-processes)
- [Kill multiple processes with a single kill -9 command](https://www.toolbox.com/tech/operating-systems/question/kill-multiple-processes-with-a-single-kill-9-command-072511/)

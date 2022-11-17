## shell

shell启动的时候会读取一些配置脚本，比如启动Login的shell会话，会读取下面一个或者多个配置文件：

- `/etc/profile`：全局配置，适用所有用户
- `~/.bash_profile`：当前用户，可以扩展或者重载全局配置
- `~/.bash_login`：如果没有找到`~/.bash_profile`，那么尝试读取该脚本文件
- `~/.profile`：如果`~/.bash_profile`和`~/.bash_login`都没有找到，那么尝试读取该文件

如果启动Non-login的shell会话，会读取：

- `/etc/bash.bashrc`：全局配置，适用所有用户
- `~/.bash_profile`：当前用户，可以扩展或者重载全局配置

我们可以通过`printenv`把shell会话启动之后设置的环境变量打印出来。

参考：

- [Difference between Login Shell and Non-Login Shell?](https://unix.stackexchange.com/questions/38175/difference-between-login-shell-and-non-login-shell)
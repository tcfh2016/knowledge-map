## I/O

使用`read text`就可以从键盘读取数据并将读取到的内容保存到变量text中。`read`命令有几个常见的参数：

- `-p`：在获取输入前提前打印一些提示，比如`read -p "Enter some text > " text`。
- `-t`：指定等待输入的时间，按秒计，比如`read -t 3 response`。
- `-s`：不显示出用户的输入内容，这在提示用户输入密码的时候为了隐私是必要的。

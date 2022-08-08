##

```
os.system("sh test.sh")

import subprocess
# On Python 3.4 and earlier
output = subprocess.call(["./test.sh","xyz","1234"])
# After Python
output = subprocess.run(["./test.sh","xyz","1234"])
```

发现一个问题：手动在shell终端执行python脚本，里面去调用`test.sh`没有问题，但是配置为cron自动任务就不成功。之后发现是因为权限不足所致，使用`chmod 777 test.sh`将其修改为可执行之后能够正常执行。

参考：

- [How do I execute a program or call a system command?](https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command)

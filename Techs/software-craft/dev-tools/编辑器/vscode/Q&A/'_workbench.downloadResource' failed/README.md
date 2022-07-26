Remote多次尝试连接失败，提示“If you continue to see this message, you can try toggling the remote.SSH.useFloc/Error: Running the contributed command: ‘_workbench.downloadResource‘ failed”

在[vscode ssh连接失败](https://blog.csdn.net/myWorld001/article/details/119443079)阅读到连接失败可能是因为remote server上无法下载更新文件，于是尝试将remote server上的`~/.vscode-server`目录删除后重新连接，提示：

![](./vscode_connect_remote_fail.PNG)

看到确实是下载问题，所以再浏览到[Troubleshooting hanging or failing connections](https://code.visualstudio.com/docs/remote/troubleshooting#_troubleshooting-hanging-or-failing-connections)里面提到通过设置VSCODE的配置文件setting.json来让SSH一直使用本地网络下载，即配置`"remote.SSH.localServerDownload": "always"`,尝试之后发现还是不可以。

不过尽管有着如上的错误，但是无法进一步定位到是下载什么资源出错了，几番搜索之后找到[这里](https://github.com/microsoft/vscode-remote-release/issues/4743)里面提到了打开“Help > Toggle Developer Tools > Console”然后在里面看到了更详细的日志信息，发现是在下载vscode-server-linux-x64.tar.gz的时候有问题，不过我本地下载是可以的，那为什么我上面已经配置了"remote.SSH.localServerDownload": "always"还是不行呢？

![](./vscode-server-download-fail.PNG)

仔细看了下terminal上的日志，发现已经是在尝试在本地下载，但是依然出错。

> [16:59:57.601] Got request to download on client for {"platform":"linux","arch":"x64","destFolder":"/home/lianbche/.vscode-server/bin/7f6ab5485bbc008386c4386d08766667e155244e"}
[16:59:57.602] Downloading VS Code server locally...
[16:59:58.815] Resolver error: Error: Running the contributed command: '_workbench.downloadResource' failed.
	at _executeContributedCommand (c:\Users\lianbche\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\workbench\services\extensions\node\extensionHostProcess.js:94:111039)

后面仿照[VS Code的Error: Running the contributed command: ‘_workbench.downloadResource‘ failed解决](https://www.cnblogs.com/LiuYanYGZ/p/15030165.html)这篇文章来操作之后连接成功。有下面几步：

- step 1: 根据console里面的URL下载对应的软件包，比如这次的vscode-server-linux-x64.tar.gz
- step 2: 登录到remote server，进入`/home/my_account/.vscode-server/bin/seems-SHA1-named-folder`
- step 3：将vscode-server-linux-x64.tar.gz拷贝到上面的folder里面并解压。*注：如果解压后生成了新的名为vscode-server-linux-x64的目录，你需要将目录下所有文件拷贝到.vscode-vserver/bin/seems-SHA1-named-folder下面*
- step 4：重新连接，成功。

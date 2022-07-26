## Windows安装更新后，重启连接不成功，提示`failed to create hard link`

```
> ln: failed to create hard link ‘/home/lianbche/.vscode-server/bin/3b889b090b5ad5
> 793f524b5d1d39fda662b96a2a/vscode-remote-lock.lianbche.3b889b090b5ad5793f524b5d1
> d39fda662b96a2a’Installation already in progress...
```

在[VS code can't ssh to server: failed to create hard link](https://stackoverflow.com/questions/60868067/vs-code-cant-ssh-to-server-failed-to-create-hard-link)看到只需要去把上面提示的lock文件删掉，再重新连接即可。

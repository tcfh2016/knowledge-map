## SSH

## SSH publickey

在访问代码仓库的时候如果提示“Permission denied (publickey)”的错误，那么可能是SSH没有设定，此时需要在访问的设备上使用命令`cd ~/.ssh && ssh-keygen`生成SSH公钥并拷贝到被访问服务器上：

参考：

- [Git: How to solve Permission denied (publickey) error when using Git?](https://stackoverflow.com/questions/2643502/git-how-to-solve-permission-denied-publickey-error-when-using-git)

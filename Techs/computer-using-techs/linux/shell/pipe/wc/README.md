## wc

`wc`命令用来统计文件的行数（`-l`）、单词（`-w`）、字节数（`-c`），使用格式为`wc [OPTION]... [FILE]...`。

当然，它可以摇身一变用来统计当前目录的文件个数：

```
ls . | wc -l
ls -1 | wc -l
ls -l . | egrep -c '^-'
```

参考：

- [wc command in Linux with examples](https://www.geeksforgeeks.org/wc-command-linux-examples/)
- [How To Count Files in Directory on Linux](https://devconnected.com/how-to-count-files-in-directory-on-linux/)
- [Count number of files within a directory in Linux? ](https://stackoverflow.com/questions/20895290/count-number-of-files-within-a-directory-in-linux)
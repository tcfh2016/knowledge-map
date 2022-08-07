## tar

`tar`工具是一款打包工具，它在工作时可以调用其他的压缩程序来进行压缩。比如调用gzip来压缩之后的后缀名为".tar.gz"，调用bzip2压缩之后的文件包后缀名为".tar.bz2"。

### 打包并压缩

```
tar -cvf prefix.tar source_directory
tar -czvf prefix.tar.gz source_directory
tar -czvj prefix.tar.bz2 source_directory
```

- -c, --create: create a new archive
- -z, --gzip: filter the archive through gzip
- -j, --bzip2:  filter the archive through bzip2
- -v, --verbose: verbosely list files processed
- -f, --file=ARCHIVE: use archive file or device ARCHIVE（*注：制定包文件名。*）

### 解压

```
tar -xvzf glibc.tar.gz -C target_directory
tar -xvjf glibc.tar.bz2 -C target_directory
```

这里的参数：

- -x, --extract:  extract files from an archive
- -z, --gzip: filter the archive through gzip
- -j, --bzip2:  filter the archive through bzip2
- -v, --verbose: verbosely list files processed
- -f, --file=ARCHIVE: use archive file or device ARCHIVE（*注：制定包文件名。*）

### 其他

- -t,--list 列出备份文件的内容。
- -f, --file=<备份文件> 指定备份文件。

比如`tar -tf TestLog.tgz`会列出TestLog.tgz这个压缩包里面的所有文件，包括子目录。

- -C<目的目录>,--directory=<目的目录> 切换到指定的目录。

比如`tar -C target -xzvf package selected_files`是将package里面的选中的`selected_files`解压到target目录中。

参考：

- [Linux tar 命令](https://www.runoob.com/linux/linux-comm-tar.html)

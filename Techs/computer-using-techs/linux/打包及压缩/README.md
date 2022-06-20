## tar

`tar`工具是一款打包工具，它在工作时可以调用其他的压缩程序来进行压缩。比如调用gzip来压缩
之后的后缀名为".tar.gz"，调用bzip2压缩之后的文件包后缀名为".tar.bz2"。

### 1 打包并压缩

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

### 2 解压

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

## zip/unzip

加压到指定目录：

unzip -d ./python_package_jack python_package_jack.zip

## zip

通过`zip archive.zip file1 file2 file3`可以一次性压缩多个文件，但怎么写一个循环来批量压缩指定的文件呢？

- `-r`参数是用来压缩整个目录的。
- `-j`参数忽略压缩文件的原始目录。

请注意下面两者的区别，第一条命令会出现“zip warning: name not matched”的错误，原因在于`zip_files`是一个包含多个文件名的变量，使用`"${zip_files}"`会将这个包含多个文件名的字符串当成单个文件名称，所以会出错。

```
zip -j "${my_path}/CI_SCT/${filename}.zip" "${zip_files}"
zip -j "${my_path}/CI_SCT/${filename}.zip" ${zip_files}
```

参考：

- [How To Zip Multiple Files on Linux](https://devconnected.com/how-to-zip-multiple-files-on-linux/)
- [zip warning - name not matched](https://stackoverflow.com/questions/46015202/zip-warning-name-not-matched)
- [zip -j command, what does the -j option mean?](https://stackoverflow.com/questions/2851846/zip-j-command-what-does-the-j-option-mean)


## unzip

如果当前系统中没有`unzip`那么可以使用`apt-get install unzip`来安装。加压常用的参数为：

-j 不处理压缩文件中原有的目录路径。
-o 不必先询问用户，unzip执行后覆盖原有文件。
-d<目录> 指定文件解压缩后所要存储的目录。

如果不是解压所有的文件，而是其中的部分，那么就需要指定zip文件中的文件路径才能正常解压。

```
# 将zip解压到指定的目录
unzip -d ./python_package_jack python_package_jack.zip

# 没有指定压缩包内的路径，无法工作
unzip -jo output.zip "changes.csv" -d "./get_build"

# 指定路径，可以工作
unzip -jo output.zip "*/*/changes.csv" -d "./get_build"
```

执行`unzip`之后需要删除之前的zip文件，似乎没有命令支持，而是需要另外进行删除操作。

参考：

- [Extract a single file from a zip file only knowing the extension](https://unix.stackexchange.com/questions/220586/extract-a-single-file-from-a-zip-file-only-knowing-the-extension)

## zip/unzip

```
apt-get install unzip
```

加压到指定目录：

-j 不处理压缩文件中原有的目录路径。
-o 不必先询问用户，unzip执行后覆盖原有文件。
-d<目录> 指定文件解压缩后所要存储的目录。
[.zip文件] 指定.zip压缩文件。
[文件] 指定要处理.zip压缩文件中的哪些文件。

unzip -d ./python_package_jack python_package_jack.zip

```
# 没有指定压缩包内的路径，无法工作
unzip -jo output.zip "changes.csv" -d "./get_build"
# 指定路径，可以工作
unzip -jo output.zip "*/*/changes.csv" -d "./get_build"
```

参考：

- [Extract a single file from a zip file only knowing the extension](https://unix.stackexchange.com/questions/220586/extract-a-single-file-from-a-zip-file-only-knowing-the-extension)

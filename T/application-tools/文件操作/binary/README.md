## 二进制文件操作

二进制文件无法直接通过文本编辑器打开进行查看，因为文本编辑器默认是以ascii或其他格式展示的，已经是对原始二进制文件解析之后的结果，所以经常可见一些乱码。

可以使用如下命令：

```
xxd file_name        # 十六进制展示
hexdump -C file_name # 十六进制展示

xxd -b file_name     # 二进制格式展示
```

参考：

- [](https://stackoverflow.com/questions/1765311/how-to-view-files-in-binary-from-bash)

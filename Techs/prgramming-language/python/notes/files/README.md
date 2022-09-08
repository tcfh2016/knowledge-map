## 文件的分类

文件通常存储在硬盘、U 盘、闪存条等辅助存储设备中，是一个命名的比特集合，它们通常分为文本文件和二进制文件两种类型。

|文本文件|二进制文件|
|-|-|
|基本是磁盘中的字符串，人类可直接阅读并编辑|人类无法阅读和编辑|
|程序无法直接阅读|程序更容易阅读，特定的格式对应特定的程序|
|文件相对较大，常需要压缩|占用空间相对较少|

`os`、`os.path`提供了与文件/文件夹操作函数。


## 常见问题

### 如何快速得知一个文件的行数

```
num_lines = sum(1 for line in open('myfile.txt'))
```

参考：

- [How to get line count of a large file cheaply in Python?](https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python)

### 如何在写入文件的时候携带格式化参数

现准备好格式化好了的string，再写入。

参考：

- [](https://realpython.com/python-string-formatting/)

### 如何仅读取文件开头或者结尾几行？

有时候调试需要打印文件内容，如果文件内容较多则会刷屏，没有shell里面直接`head`那样的内容，可以通过控制打印的行数来控制：

```
with open("file.txt", 'r') as f:
  cnt = 0
  for line in f:
    cnt += 1
    if (cnt > 5):
      break
    print(line)
```

## 参考阅读

- [Miscellaneous operating system interfaces](https://docs.python.org/2.7/library/os.html)
- [How do I check if directory exists in Python?](https://stackoverflow.com/questions/8933237/how-do-i-check-if-directory-exists-in-python)

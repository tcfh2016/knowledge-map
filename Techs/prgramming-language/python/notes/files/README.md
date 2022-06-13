## 一、文件的分类

文件通常存储在硬盘、U 盘、闪存条等辅助存储设备中，是一个命名的比特集合，它们通常分为文本
文件和二进制文件两种类型。


|文本文件|二进制文件|
|-|-|
|基本是磁盘中的字符串，人类可直接阅读并编辑|人类无法阅读和编辑|
|程序无法直接阅读|程序更容易阅读，特定的格式对应特定的程序|
|文件相对较大，常需要压缩|占用空间相对较少|

## 二、文件/文件夹的操作

`os`、`os.path`提供了与文件/文件夹操作函数：

- os.getcwd() 返回当前工作目录的名称。
- os.listdir(p) 返回一个字符串列表，包含路径p指定的文件夹下所有的文件和文件夹名称。
- os.chdir(p) 将当前工作目录切换至p。
- os.path.isfile(p) 判断当前p是否为文件。
- os.path.isdir(p) 判断当前p是否为文件夹。
- os.stat(fname) 返回有关fname的信息。

文件的读写操作需要指定特定的模式：

|字符|含义|
|-|-|
|'r'|为读取而打开文件（默认模式）|
|'w'|为写入而打开文件|
|'a'|为在文件末尾附加而打开文件|
|'b'|二进制模式|
|'t'|文本模式|
|'r+'|为读写打开文件|

文本文件的读取可以按照一行甚至是整个文件内容作为大型字符串的方式读取，而二进制文件的读取
方式则可以按照每个字节进行。

## 判断文件是否可用

```
if os.access("myfile", os.R_OK):
  with open("myfile") as fp:
    return fp.read()
```

## 读文件

文件读取可以使用多个方法：

- `myfile.read(size)`：一次读取size个字节，不指定size就读取整个文件
- `myfile.readline()`：一次仅读取一行
- `myfile.readlines()`：一次仅读取文件所有行，并保存为一个字符串list

文件的读取支持多种方式，如果要一行一行地扫描一个文本文件，文件迭代器往往是最佳选择：

```
for line in open('myfile'):
  print(line, end='')
```

## 写文件

```
lines = (
  'Line1: xxx',
  'Line2: xxx'
  )
with open('written.txt', mode='w') as out_file:
  out_file.write('hello')

  out_file.writelines(lines)
  out_file.flush() # 正式写入

with open('written.txt', mode='a') as out_file:
  out_file.write('hello')  
```


## 三、常见问题

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

[Miscellaneous operating system interfaces](https://docs.python.org/2.7/library/os.html)

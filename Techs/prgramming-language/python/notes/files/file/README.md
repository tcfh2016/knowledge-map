## 文件操作

- os.path.isfile(p) 判断当前p是否为文件。
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

文本文件的读取可以按照一行甚至是整个文件内容作为大型字符串的方式读取，而二进制文件的读取方式则可以按照每个字节进行。


```
# 判断文件是否可用
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

参考：

- [How do I check if directory exists in Python?](https://stackoverflow.com/questions/8933237/how-do-i-check-if-directory-exists-in-python)
- [Create a directory in Python](https://www.geeksforgeeks.org/create-a-directory-in-python/)

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


## [读文件](./read/README.md)



## [写文件](./write/README.md)

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

with open(input_txt, 'r') as f1, open(output_txt, 'w') as f2, open(mandatory_caselist, 'w') as f3:

for line in f1.readlines():
pass

```

参考：

- [How do I check if directory exists in Python?](https://stackoverflow.com/questions/8933237/how-do-i-check-if-directory-exists-in-python)
- [Create a directory in Python](https://www.geeksforgeeks.org/create-a-directory-in-python/)

## `illegal multibyte sequence`错误

```
open("text.txt", "w", encoding="utf-8")
```


## 读文件

常用方法：

- `myfile.read(size)`：一次读取size个字节，不指定size就读取整个文件
- `myfile.readline()`：一次仅读取一行
- `myfile.readlines()`：一次仅读取文件所有行，并保存为一个字符串list
- `myfile.seek(offset[, whence])`：offset表示文件的起始位置，whence为0代表绝对位置，1代表相对“当前的”位置，2代表相对“文件末尾”

文件的读取支持多种方式，如果要一行一行地扫描一个文本文件，文件迭代器往往是最佳选择：

```
for line in open('myfile'):
  print(line, end='')
```


## 如何读取文件第一行和最后一行？

最直接的方式，是把整个文件读取到

```
with open(filename, 'r') as fh:
    lines = fh.readlines()
    first = lines[0]
    last = lines[-1]    
```

当然，还有更高效的方式：

```
def readlastline(f):
    f.seek(-2, 2)              # Jump to the second last byte.
    while f.read(1) != b"\n":  # Until EOL is found ...
        f.seek(-2, 1)          # ... jump back, over the read byte plus one more.
    return f.read()            # Read all data from this point on.
    
with open(file, "rb") as f:
    first = f.readline()
    last = readlastline(f)
```

参考：

- [What is the most efficient way to get first and last line of a text file?](https://stackoverflow.com/questions/3346430/what-is-the-most-efficient-way-to-get-first-and-last-line-of-a-text-file)
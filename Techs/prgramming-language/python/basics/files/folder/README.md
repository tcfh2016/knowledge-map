## 文件夹操作

- os.getcwd() 返回当前工作目录的名称。
- os.listdir(p) 返回一个字符串列表，包含路径p指定的文件夹下所有的文件和文件夹名称。
- os.chdir(p) 将当前工作目录切换至p。
- os.path.isdir(p) 判断当前p是否为文件夹。
- os.path.isfile(p) 判断当前p是否为文件。
- os.mkdir(p) 创建文件夹。
- os.path.join 

```
os.path.isdir('new_folder')
```

## 判断文件夹是否为空

两种方法：

```
if len(os.listdir('/your/path')) == 0:
    print("Directory is empty")

if not os.listdir('/your/path'):
    print("Directory is empty")
```

因为当目录不存在的时候`listdir`会抛出异常，所以最好先做下保护：

```
if os.path.isdir(dir_name):
    if not os.listdir(dir_name):
        print("Directory is empty")
```


参考：

- [How to check if folder is empty with Python?](https://stackoverflow.com/questions/49284015/how-to-check-if-folder-is-empty-with-python)


## `os.mkdir()`和`os.makedirs()`的区别

前者仅创建单层目录，后者可以根据路径创建多层目录。

- [What is different between makedirs and mkdir of os?](https://stackoverflow.com/questions/13819496/what-is-different-between-makedirs-and-mkdir-of-os)


## 为什么需要`os.path.join()` ？

这是因为在不同操作系统下对应的文件路径是不同的，比如Linux下面是`/home/me/work`这种形式，但是在Windows下面则是`C:\Users\me\work`这种形式。

所以，如果你要编写在两种系统下都能够正确访问文件系统的代码，那么必须对路径进行拼接，这个时候就需要使用`os.path.join()`，比如通过`os.path.join("", "me", "work")`来拼接对应的操作路径。


## 创建多级目录

```
import os
path = '/home/dail/first/second/third'
os.makedirs(path, exist_ok=True)
```

参考：

- [How can I create directories recursively? ](https://stackoverflow.com/questions/6004073/how-can-i-create-directories-recursively)


## 删除操作

1）`os.remove()`删除单个文件

需要注意的是：

- 不能删除目录（文件夹），Windows下会提示`PermissionError`。
- 如果文件不存在会抛出`FileNotFoundError`异常，最好使用`os.path.isfile()`先检查。

2）`os.rmdir()`删除文件夹

只能删除单个空目录，非空目录会提示“OSError: [WinError 145] The directory is not empty”。

3）`shutil.rmtree()`删除文件夹和其中所有文件

同样的，如果文件夹不存在会抛出`FileNotFoundError`异常，可以使用`os.path.isdir()`先检查。

参考：

- [How do I delete a file or folder in Python?](https://stackoverflow.com/questions/6996603/how-do-i-delete-a-file-or-folder-in-python)
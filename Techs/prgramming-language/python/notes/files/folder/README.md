## 文件夹操作

- os.getcwd() 返回当前工作目录的名称。
- os.listdir(p) 返回一个字符串列表，包含路径p指定的文件夹下所有的文件和文件夹名称。
- os.chdir(p) 将当前工作目录切换至p。
- os.path.isdir(p) 判断当前p是否为文件夹。
- os.mkdir(p) 创建文件夹
- os.path.join 

```
os.path.isdir('new_folder')
```


## `os.mkdir()`和`os.makedirs()`的区别

前者仅创建单层目录，后者可以根据路径创建多层目录。

- [What is different between makedirs and mkdir of os?](https://stackoverflow.com/questions/13819496/what-is-different-between-makedirs-and-mkdir-of-os)


## 为什么需要`os.path.join()` ？

这是因为在不同操作系统下对应的文件路径是不同的，比如Linux下面是`/home/me/work`这种形式，但是在Windows下面则是`C:\Users\me\work`这种形式。

所以，如果你要编写在两种系统下都能够正确访问文件系统的代码，那么必须对路径进行拼接，这个时候就需要使用`os.path.join()`，比如通过`os.path.join("", "me", "work")`来拼接对应的操作路径。

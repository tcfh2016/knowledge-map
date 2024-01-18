## 命令与PATH

在我们在命令行键入命令时，系统并不会搜索所有目录去找到该命令对应的可执行文件，因为耗时太大。所以系统维护了一个路径的集合，这个集合被定义在`PATH`里面。

```
# 打印出当前的PATH，是包含了以冒号“:”作为分隔符的多个路径
echo $PATH

# 将自己需要的路径（“my_own_path”）设置到PATH里面
export PATH=$PATH:my_own_path
```

## 常见命令

- `export`是告诉shell让后面的命令对该shell所有子进程生效。
- `alias name=value`给长的命令创建短的别名，比如`alias l='ls -l'`。
- `w -h`查看登入用户的信息




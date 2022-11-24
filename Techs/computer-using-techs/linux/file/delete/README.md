## 如何保留最新的50个文件，删除其他文件

先熟悉有关删除的比较低级的用法，比如使用`ls . | xargs rm`可以将ls得到的文件列表传递给rm命令执行删除操作。

```
ls -t | tail -n +61 | xargs rm -rf
ls -rt | head -n -60 | xargs rm -rf
```

参考：

- [](https://unix.stackexchange.com/questions/209555/how-to-delete-files-from-a-folder-which-have-more-than-60-files-in-unix)


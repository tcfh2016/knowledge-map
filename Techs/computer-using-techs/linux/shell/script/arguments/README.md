## 命令行参数

可以通过`$x`来获取命令行参数：`$0`是命令的名字，`$1`是第一个参数... 同时，`$#`代表了命令行参数的个数，`$@`是所有命令行参数的列表。

```
if [ $# -gt 0 ]; then
    echo "Your command line contains $# arguments"
else
    echo "Your command line contains no arguments"
fi
```

## 入参被修改


# 需求

每次使用tti_trace_parser.exe来解析多个tti-trace文件就需要反复多次执行如下命令：

```
tti_trace_parser.exe --decode source_filename --output target_filename
```

是否可以定制更加灵活的批处理脚本呢？

# 实现

google搜索在 python里面如何调用外部程序得到可以使用 `subprocess`，尝试之下确实可行，目
前仅仅使用了最基本的调用方式：先将命令组装好，再调用`subprocess.call`执行命令。

```
source_file = os.path.join(dir, f)
    target_file = os.path.join(dir, f[:f.find(".")] + ".csv")
    command = "tti_trace_parser_wmp.exe --decode %s --output %s" %(source_file, target_file)

    subprocess.call(command)
```

# 参考阅读

- (Calling an external command in Python)[https://stackoverflow.com/questions/89228/calling-an-external-command-in-python]


# 'module' object has no attribute......

```
Traceback (most recent call last):
  File "bin2text.py", line 31, in <module>
    main()
  File "bin2text.py", line 27, in main
    par = parser.Parser(cfg)
AttributeError: 'module' object has no attribute 'Parser'
```
这种错误出现常见两种情况：

- 对应的模块里面确实没有需要的方法或者变量。
- 自己定义了与Python库重名的模块，导致名称覆盖。


# OError: [Errno 22] invalid mode ('w') or filename: '2018-07-05-14:48:06.log'

尝试使用logging模块，但是在创建日志文件的时候碰到了如下错误：

```
File "C:\Users\lianbche\Work\Git\bin2text\src\__init__.py", line 11, in <module>
  open(log_file, 'w').close()
IOError: [Errno 22] invalid mode ('w') or filename: '2018-07-05-14:48:06.log'
```

将错误信息`IOError: [Errno 22] invalid mode  or filename:`进行搜索发现原因可能是文件
名称没有使用raw字符串，但看了StackOverflow上的一篇文章提到raw字符串仅仅是让 Python解析
器对待'\'的时候不要进行转义，突然想到可能是文件名包含有不合法的符号`-`或者`:`，于是尝试
在Windows上创建包含有`-`或`:`的文件果然发现`:`非法。

```
timestamp = datetime.datetime.now()
log_file = timestamp.strftime("%Y-%m-%d-%H:%M:%S") + ".log"
# 修改为：log_file = timestamp.strftime("%Y-%m-%d-%H-%M-%S") + ".log"
open(log_file, 'w').close()
```

[python : how to convert string literal to raw string literal?](https://stackoverflow.com/questions/7262828/python-how-to-convert-string-literal-to-raw-string-literal)

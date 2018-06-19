
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

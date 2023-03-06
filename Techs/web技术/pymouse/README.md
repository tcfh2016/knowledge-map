## `ImportError: cannot import name 'PyMouse'`

脚本迁移之后不再使用之前老的`PyMouse`，会出现下面的错误，之后还出现找不到`unix`：

```
 File "/home/lianbche/.local/lib/python3.6/site-packages/pymouse/__init__.py", line 95, in <module>
    from unix import PyMouse, PyMouseEvent
ImportError: cannot import name 'PyMouse'
```

搜索之后看到说是`PyMouse`升级合并到了`PyUserInput`，执行`pip3 install PyUserInput`安装还是有同样的问题。

最后在[这里](https://www.jianshu.com/p/6ba8e4a2e464)找到答案，将已有的 `pymouse`, `pykeyboard`, `PyUserInput`全部清理掉，重新安装`PyUserInput`解决问题。

参考：

- [Cannot import name PyMouse](https://stackoverflow.com/questions/34022407/cannot-import-name-pymouse)
- [](https://github.com/SavinaRoja/PyUserInput)
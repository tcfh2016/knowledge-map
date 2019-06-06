# eval

# `if __name__ == "__main__"`代表什么意思？

查阅 StackOverFlow，得知`__name__`是每个源代码文件在执行时均有的隐式变量，当它被当做程
序执行时，该变量设置为`__main__`，当它被当做模块引入其他文件中时该变量设置为`模块名称`。

使用`__name__` 来检查模块的设计意图可以很方便地单独对文件内的功能进行测试。

参考：

- [What does if __name__ == “__main__”: do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
- [Python学习手册, 第27章：更多实例，P653]()

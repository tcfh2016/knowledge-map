# type()

显示对应数据的类型。

# eval()

内置函数`eval`能够把字符串当作可执行程序代码，可以将字符串转换成对象。但它过于强大，会简
单地执行Python的任何表达式。如果想存储Python的原生对象，但又无法信赖文件的数据来源，Python
的标准库pickle模块会是个理想的选择。

# `if __name__ == "__main__"`代表什么意思？

查阅 StackOverFlow，得知`__name__`是每个源代码文件在执行时均有的隐式变量，当它被当做程
序执行时，该变量设置为`__main__`，当它被当做模块引入其他文件中时该变量设置为`模块名称`。

使用`__name__` 来检查模块的设计意图可以很方便地单独对文件内的功能进行测试。

参考：

- [What does if __name__ == “__main__”: do?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
- [Python学习手册, 第27章：更多实例，P653]()

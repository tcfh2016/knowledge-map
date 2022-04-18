## 目录

- []()
- [POD类型](./POD/README.md)

## Q&A

- STL容器中的size()，输出类型需要使用`%zu`

- 编译时的`invalid use of incomplete type`错误

一种原因是在编译时需要对应类型的定义，但是实际上仅仅看到了前向声明。

参考：

- [error: Invalid use of incomplete type](https://stackoverflow.com/questions/38179919/error-invalid-use-of-incomplete-type)

- 如何定义类中的常量

使用static来修饰常量，如`static const int c1 = 7`。

参考：

- [How do I define an in-class constant?](https://www.stroustrup.com/bs_faq2.html#in-class)

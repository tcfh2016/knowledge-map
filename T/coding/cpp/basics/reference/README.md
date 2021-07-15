## reference

引用和指针都能够完成1、在函数类实现对传入参数指向对象的修改；2、避免大结构的值拷贝。于此同时它们具有如下区别：

- 指针可能为空，使用的时候需要添加合法性检查。但引用不可能为空。
- 指针可以进行多层次的间接访问。引用仅有单层次的间接访问。
- 指针可以重新赋值。引用不可以。
- 指针可以先定义再初始化。但引用必须在定义的时候初始化。

总的来说，引用比指针更容易使用，安全性也高一点。


参考

- [References in C++](https://www.geeksforgeeks.org/references-in-c/)
- [References](https://isocpp.org/wiki/faq/references)

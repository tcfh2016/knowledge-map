## POD

POD的全称为“Plain Old Data”，指的是那些可以用memcpy, memset等函数来操作的类似于C struct类型的数据类型。C++11中定义的POD满足以下两方面：

- 没有虚函数、虚基类、引用、多个访问控制符
- 所有的成员和基类都是POD

在《C++标准库》P279有这么一句简单的介绍：

> POD describes types that use no special C++ feature. For example, every ordinary C structure is POD.

参考：

- [PODs (generalized)](http://www.stroustrup.com/C++11FAQ.html#PODs)
- [What are POD types in C++?](https://stackoverflow.com/questions/146452/what-are-pod-types-in-c)

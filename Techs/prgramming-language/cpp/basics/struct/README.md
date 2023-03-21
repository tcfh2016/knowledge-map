## struct的初始化

在c++11的时候提供了初始化列表，所以可以使用`Foo foo =  {bunch, of, things, initialized};`来执行初始化。但是有次却提示：

```
error: could not convert '{a, b, c}' from '<brace-enclosed initializer list>' to 's'
```

这是因为自己定义的结构体被解析为了`class`，拥有自身的构造器，所以不能直接使用初始化列表。解决方案是定义对应的构造器。


参考：

- [Error when initializing a struct with a brace-enclosed initializer list](https://stackoverflow.com/questions/24751567/error-when-initializing-a-struct-with-a-brace-enclosed-initializer-list)
- [Assign values to structure variables](https://stackoverflow.com/questions/32698293/assign-values-to-structure-variables)
- [A Quick Guide to Structs in C++](https://ryanflynndev.medium.com/a-quick-guide-to-structs-in-c-72b0bb80e01e)
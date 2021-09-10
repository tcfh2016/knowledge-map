# `static`关键字简介

应用场景：

-
-
-


# 应用场景分析

## static data member

1.初始化

```
class X
{
public:
      static int i;
};
int X::i = 0; // definition outside class declaration
```

参考：

- [How to initialize a static const member in C++?](https://stackoverflow.com/questions/3531060/how-to-initialize-a-static-const-member-in-c?rq=1)

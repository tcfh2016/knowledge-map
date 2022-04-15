## `static`关键字简介

`static`定义的局部变量仅仅会初始化一次，该机制的实现可以参考[What makes a static variable initialize only once?](https://stackoverflow.com/questions/5567529/what-makes-a-static-variable-initialize-only-once)。举个例子，比如在下面的函数`go()`里面定义了一个static修饰的变量`j`：

```
void go( int x )
{
    static int j = x ;
    cout << ++j << endl ; // see 6, 7, 8
}
```

那么变量`j`只会被初始化一次，编译器的保证机制会类似于新增了`j_initialized`来确保初始化只会进行一次：

```
void go( int x ) {
  static int j;
  static bool j_initialized;

  if (!j_initialized) {
    j = x;
    j_initialized = true;
  }

  ...
}
```

## 应用场景分析

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

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

以上这种较为复杂的定义方式已经在`C++17`里面得到了优化，因为你可以使用`inline`关键字直接在类里面定义的时候初始化这个变量，比如上面变量`i`的定义可以写成`static inline int i = 0`。

参考：

- [How to initialize a static const member in C++?](https://stackoverflow.com/questions/3531060/how-to-initialize-a-static-const-member-in-c?rq=1)
- [How do inline variables work?](https://stackoverflow.com/questions/38043442/how-do-inline-variables-work)

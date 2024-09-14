## `const`和`constexpr`什么区别？

两个关键字均可以用于修饰对象和函数。`constexpr`是c++11中新引入的关键字。

1）修饰对象

`const`定义的对象在初始化不能再更改。如果在定义某个变量的时候需要用到常量表达式，那么就可以用`constexpr`来修饰。

常量表达式的定义在[C++11 constexpr：验证是否为常量表达式](http://c.biancheng.net/view/7781.html)里面讲解得很清楚：常量表达式，指的就是由多个（≥1）常量组成的表达式，它在编译时候就已经出结果了。

```
int url[10];//正确
int url[6 + 4];//正确

int length = 6;
int url[length];//错误，length是变量
```

那是否使用`constexpr`的区别在哪里呢？比如下面的代码可以正常运行，但是如果把`constexpr`删掉，那么就会提示错误，因为num的值在编译的时候还没有确定。

```
constexpr int num = 1 + 2 + 3;
int url[num] = {1,2,3,4,5,6};
```


2）修饰函数

`const`可以修饰non-static成员函数，保证该函数不修改non-static数据成员。

`constexpr`既可以修饰成员函数，也可以修饰非成员函数，但需要满足一些条件，有些多。


参考：

- [What's the difference between constexpr and const?](https://stackoverflow.com/questions/14116003/whats-the-difference-between-constexpr-and-const)
- [C++11 constexpr：验证是否为常量表达式](http://c.biancheng.net/view/7781.html)

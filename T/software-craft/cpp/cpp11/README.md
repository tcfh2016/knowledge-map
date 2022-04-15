### 常规

1）初始化列表。

2）auto关键字，完成类型推导。

`auto`关键字的使用方便直接通过表达式进行类型推导，不过在涉及到引用的时候需要显示的指定`&`。否则，即便某个函数的返回值为引用，一定要使用`auto &`才能够获取到该函数返回的引用，仅仅使用`auto`是不行的。

在[Deducing the type of variable from its initializer expression](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2006/n1984.pdf)里面有如下描述：

> Thus, as in the rest of the language, value semantics is the default, and reference semantics is provided through consistent use of &.

下面是文章中的例子：

```
int foo();
auto x1 = foo(); // x1 : int
const auto& x2 = foo(); // x2 : const int&
auto& x3 = foo(); // x3 : int&: error, cannot bind a reference to a temporary

float& bar();
auto y1 = bar(); // y1 : float
const auto& y2 = bar(); // y2 : const float&
auto& y3 = bar(); // y3 : float&
```


3）range-based for循环。

###　迭代器
- cbegin()/cend()。

# 常见问题

## 编译提示` error: ‘move’ is not a member of ‘std’`

在编译一个c++11的例子的时候提示出错，只有查找是编译c++11时需要在编译选项中指定对应的编译
选项：

```
g++ move_semantics_test.cpp -std=c++11 -o move_semantics_test
```

参考：

- [C++ linux : error: ‘move’ is not a member of ‘std’ how to get around it?](https://stackoverflow.com/questions/7251251/c-linux-error-move-is-not-a-member-of-std-how-to-get-around-it)
- [What is std::move(), and when should it be used?](https://stackoverflow.com/questions/3413470/what-is-stdmove-and-when-should-it-be-used)

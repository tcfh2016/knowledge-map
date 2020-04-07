# 索引

# 经验

## 1.合理使用类型定义来提升开发效率

比如`vector<Widget>::iterator i = find(vw.begin(), vw.end(), bestWidget)`可以替换为：

```
typedef vector<Widget> WidgetContainer;
typedef WidgetContainer::iterator WCIterator;

WCIterator i = find(vw.begin(), vw.end(), bestWidget)
```

从C++11开始，`using`关键字被用来定义类型别名，主要是为了解决模板别名的命名问题，因为使用`typedef`无法给模板取别名。

```
template<typename T>
typedef int (*PFT)(T);      // error

template<typename T>
using PFT2 = int (*)(T);   // OK
```

参考：

- [What is the difference between 'typedef' and 'using' in C++11?](https://stackoverflow.com/questions/10747810/what-is-the-difference-between-typedef-and-using-in-c11)
- [C++ 关键词：using](https://zh.cppreference.com/w/cpp/keyword/using)

# 疑问

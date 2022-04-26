## lambda

`lambda`表达式可以用来定义内联的函数功能，其定义式可以被当作参数或者本地对象来使用。这项功能是在C++11的时候引入。

## 语法格式

1）简单式

```
[...] {...}
```

`[...]`为lambda introducer（捕获子句），`{...}`为lambda body（lambda主体）。如果需要在lambda表达式里面访问外部的非静态对象，就需要在`[...]`指定它们，否则保持为空即可。在指定捕获对象的时候也分按值（`[=]`）或者按引用（`[&]`）传递。

```
int x = 0;
int y = 0;

//"x"按值访问，如果将"x"替换为"="，那么除了y按引用访问，其他的外部变量都按值访问。
auto e = [x, &y] {std::couot <<x+y << std::endl; ++y;}
```

2）复杂式

复杂式是在introducer和body之间可以插入参数、mutable、exception和返回值类型。

```
[...] (...) mutable(optional) throwSpec(optional) -> retType(optional) {...}
```

## 在class或者在function中



## lambda与STL


## lambda与并行编程

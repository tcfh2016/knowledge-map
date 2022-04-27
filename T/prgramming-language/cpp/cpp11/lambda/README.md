## lambda

`lambda`表达式可以用来定义内联的函数功能，其定义式可以被当作参数或者本地对象来使用。这项功能是在C++11的时候引入。lambda的语法格式如下：

```
[...] (...) mutable(optional) throwSpec(optional) -> retType(optional) {...}
```

`[...]`为lambda introducer（捕获子句），`{...}`为lambda body（lambda主体）。

如果需要在lambda表达式里面访问外部的非静态对象，就需要在`[...]`指定它们，否则保持为空即可。在指定捕获对象的时候也分按值（`[=]`）或者按引用（`[&]`）传递。

另外比较复杂的是在introducer和body之间可以插入参数、mutable、exception和返回值类型。


## 无参数，无捕获的lambda

```
[] {
  std::cout <<"I'm the first simple lambda expression!" <<std::endl;
};
```

上面这样就定义了一个最简单的表达式，功能就是打印一句话，只不过这个只有定义，我们没有调用它，所以在运行程序时不会有任何输出。为了运行它，有两种方法：

```
// 定义时调用
[] {
  std::cout <<"I'm the second simple lambda expression!" <<std::endl;
}();

// 将lambda定义赋值给变量，然后像使用函数一样调用它
auto l = [] {
  std::cout <<"I'm the third simple lambda expression!" <<std::endl;
};
l();
```

## 带有参数的lambda

lambda既然声称为一种内嵌式的函数，那么自然它也可以接受参数，这种方式与常见函数没有什么不同。下面例子中的`x`如果以值传递，那么不会改变lamda函数定义外面的值，按值传递就会改变。

```
auto la = [](int x) {
  std::cout <<x <<std::endl;
  x = 200;
};

auto a = 100;
la(a);
la(a);
```

## 带有捕获的lambda

```
int x = 0;
int y = 0;

//x按值访问，y按引用访问
auto e = [x, &y] {std::couot <<x+y << std::endl; ++y;}

//x, y都按值访问
auto e = [=] {std::couot <<x+y << std::endl; ++y;}

//x, y都按引用访问
auto e = [&] {std::couot <<x+y << std::endl; ++y;}

//除了y按引用访问，其他的外部变量都按值访问
auto e = [=, &y] {std::couot <<x+y << std::endl; ++y;}

//编译错误，因为无法捕获到x
auto e = [&y] {std::couot <<x+y << std::endl; ++y;}
```

## lambda与STL


## lambda与并行编程

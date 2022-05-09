## lambda

`lambda`表达式可以用来定义内联的函数功能，其定义式可以被当作参数或者本地对象来使用。这项功能是在C++11的时候引入。lambda的语法格式如下：

```
[...] (...) mutable(optional) throwSpec(optional) -> retType(optional) {...}
```

`[...]`为lambda introducer（捕获子句），`{...}`为lambda body（lambda主体）。

如果需要在lambda表达式里面访问外部的非静态对象，就需要在`[...]`指定它们，否则保持为空即可。在指定捕获对象的时候也分按值（`[=]`）或者按引用（`[&]`）传递。

另外比较复杂的是在introducer和body之间可以插入参数、mutable、exception和返回值类型。


## 最简单的lambda表达式

```
[] {
  std::cout <<"I'm the first simple lambda expression!" <<std::endl;
};
```

上面这样就定义了一个最简单的表达式，功能就是打印一句话，只不过这个只有定义，我们没有调用它，所以在运行程序时不会有任何输出。为了运行它，有以下两种方法：

```
// 定义时调用
[] {
  std::cout <<"I'm the second simple lambda expression, call me now!" <<std::endl;
}();

// 将lambda定义赋值给变量，然后像调用函数一样调用它
auto l = [] {
  std::cout <<"I'm the third simple lambda expression!" <<std::endl;
};
l();
```

上面的这对中括号`[]`和大括号`{}`是lambda表达式的最低配置，其中：

- `[]`是`lambda introducer`，简称lambda导入器
- `{}`是`lambda body`，为lambda主体

看到它们我们应该马上知道它就是一个lambda表达式。


## 带有参数的lambda

lambda既然为一种内嵌式的函数，那么自然它也可以接受参数，这种方式与常见函数没有什么不同。下面例子中的`x`如果以值传递，那么不会改变lamda函数定义外面的值，按值传递就会改变。

```
auto la = [](int x) {
  std::cout <<x <<std::endl;
  x = 200;
};

auto a = 100;
la(a);
la(a);
```

以上第一次调用和第二次调用的输出均为“100”，因为lambda参数按照值传递，并没有修改变量`a`的值。但如果我们将参数从`int x`修改为`int& x`那么第二次调用的输出为“200”，也就是变量`a`的值在第一次调用lambda的时候被修改了。*注：lambda不能被定义为模板，它的每种参数类型必须要显示指定。*


## 带有返回值的lambda

同样地，既然函数同时可知参数和返回值，lambda也可以带有返回值。当你没有指定返回值类型的时候，它会根据实际返回的类型进行推导：

```
auto l1 = [] { return 99.99; }; // 输出：99.99
auto l1 = []() ->int { return 99.99; }; // 输出：99
```

需要注意的是在显示指定返回类型的时候，你必须要将lambda的表达式写得较为正式化，也就是必须带上函数参数的`()`（即便没有参数），以及`-> int`用来指定函数返回值类型。


## 带有捕获的lambda

什么是“捕获”？我们知道在一个函数体内部要访问函数体外部的变量有两种方式：第一种是通过参数将变量传递进来；第二种是直接访问函数体之外作用域的变量（在C语言里面函数体内部可以直接访问外部变量，在C++语言里面的class可以访问class的成员变量）。

那么这里的“捕获”类似于如上的第二种，它提供了一种访问lambda表达式外部变量的机制。你可以为特定变量指定“按值捕获”或者“按引用捕获”，也可以为所有外部变量进行指定，尽管这并不是一种推荐的做法。

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

当然，或许，理解捕获并不是那么简单，起码我最开始理解错误了。因为这里还涉及到捕获的时机，比如下面的代码的输出我最初以为第二次lambda调用的输出是`a = 99, b = 100`，但实际上确是`a = 0, b = 100`，这里面的原因是*lambda对于外部变量的捕获时机是在定义的时候就决定了，而不是在调用的时候*。

```
int a = 0;
int b = 1;
auto l = [a, &b] {
  std::cout <<"a = " <<a << std::endl;
  std::cout <<"b = " <<b << std::endl;
  ++b;
};
a = 99;
b = 99;
l(); // 输出a = 0, b = 99
l(); // 输出a = 0, b = 100
```

## lambda与STL


## lambda与并行编程

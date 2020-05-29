# 函数模板


## 定义模板函数

函数模板提供了一种函数行为，该函数行为可以用多种不同的类型进行调用。定义的函数模板不会被编译成单个处理任何类型的函数，而是根据调用的实际情况产生出多个不同的函数（实体）。这里面用具体类型代替模板的过程成为“实例化(instantiation)”。

```
template <typename T>
inline T const& max(T const& a, T const& b)
{
  return a < b ? b : a;
}
```

函数模板有两种类型的参数：“模板参数”和“用参数”。前者位于函数模板名称前，在一对尖括号中声明，比如上面代码中的`<typename T>`；后者位于函数模板名称后，在一对圆括号内部声明，如`(T const& a, T const& b)`。


## 使用模板函数

模板函数使用的时候通常直接像普通函数一样调用即可，比如`max(1,2)`，此时编译器会根据调用时候实参的类型构造对应的函数示例。

也可以直接指定特定的类型来显示地实例化函数模板，比如`max<double>(1.2, 2)`。


## 重载函数模板

和普通函数一样，函数模板也可以被重载。也就是说，相同的函数名称可以具有不同的函数定义，在使用函数名称进行调用的时候编译器会决定使用哪个候选函数。

```
int const& max(int const&a, int const&b)
{
  return a < b ? b : a;
}

template <typename T>
T const& max(T const&a, T const&b)
{
  return a < b ? b : a;
}
```

如上所示，一个非模板函数可以和一个同名的函数模板同时存在。在调用的时候，如果其他条件都相同，重载解析通常会调用非模板函数，而不会从该模板产生出相同的实例，比如我们这里使用`max(1,2)`会显示调用重载的int版本函数。*可以使用max<>(1,2)来让函数模板生成基于int的示例。*

但是，如果我们使用`max('a', 'b')`的时候，那么如上的模板函数会产生出不同于`int max(int, int)`的实例。

## 常见问题

### 1.调用重载函数的时候的结果可能与该重载函数在此时是否可见有关。

```
template <typename T>
T const& max(T const&a, T const&b)
{
  return a < b ? b : a;
}

template <typename T>
T const& max(T const&a, T const&b, T const&c)
{
  return max(max(a,b), c); // 由于此时重载的int版本不可见，这里会优先使用模板函数。
}

int const& max(int const&a, int const&b)
{
  return a < b ? b : a;
}
```

### 2.编译错误“explicit specialization in non-namespace scope”

编写代码的时候出现这个错误，查找之下可能的原因有两个：

- gcc不允许在class内部进行函数模板的全特化
- gcc在class内部进行函数模板全特化必须要以class进行特化为前提，这是gcc的一个问题，在C++17之后修复。

我的问题里并不是在模板类里面全特化成员函数，而是普通类。因此，只能按照第一种思路去解决，替代方案是将“函数全特化”修正为“重载函数模板”。

参考：

- [Explicit specialization in non-namespace scope [duplicate]](https://stackoverflow.com/questions/3052579/explicit-specialization-in-non-namespace-scope)
- [C++ syntax for explicit specialization of a template function in a template class?](https://stackoverflow.com/questions/2097811/c-syntax-for-explicit-specialization-of-a-template-function-in-a-template-clas)
- [Explicit specialization in non-namespace scope does not compile in GCC](https://stackoverflow.com/questions/49707184/explicit-specialization-in-non-namespace-scope-does-not-compile-in-gcc)


### 2.

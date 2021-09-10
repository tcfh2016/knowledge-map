## Trait技法

在Trait技法之前需要理解模板偏特化（只针对类模板，函数模板仅有重载），其定义是：如果类模板拥有一个以上的模板参数，那么可以针对其中的部分参数进行特化，也即提供特化版本的实现。需要留意的是这里的“偏特化”并不是给类模板指定特别的参数来进行实例化，而是提供了另外一种模板的定义方法，这种定义对模板参数增加了新的限制。

比如下面这个例子，开头的类模板支持所有类型，但后面的类模板仅仅支持原生指针类型。它们两者都是类模板，只不过后者接收的类型是前者的一个子集：

```
template <typename T>
class C
{
  ...
}

template <typename T>
class C<T*>
{
  ...
}
```

为此，我们可以利用类模板这种偏特化的特性专门创建偏特化的类来获取到特别的类型。比如下面的`MyClass`是一个模板类，它可以被实例化为不同的类型，但不管它被实例化为哪种类型，我们都可以通过`Traits<T>::value_type`来获取到特定的类型。

```
template <typename T>
class MyClass
{
  using value_type = T;
}

template <typename T>
struct Traits
{
  using value_type = T::value_type
}
```

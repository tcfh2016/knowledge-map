## Type Traits

C++标准库里面的实现几乎都是基于模板，为了更好的支持模板编程，一些常见的模板应用被发明了出来。type traits是用来给不同类型定义不同行为的发明之一。


## Type Traits的目的

一种Type Trait是一个可以根据类型来展现不同特性的模板实现，它通常根据传入的一个或者多个参数得出某种类型或者值（更多的是类型）。比如下面的函数可以根据传入的参数是否为指针来进行不同的处理：

```
template <typename T>
void foo (const T& val)
{
  if (std::is_pointer<T>::value) {
    std::cout <<"calls for a pointer" <<std::endl;
  }
  else {
    std::cout <<"calls for a value" <<std::endl;
  }
}
```

因为`std::is_pointer`要么返回`std::true_type`要么返回`std::false_type`，所以上面的这个例子还可以这么实现（*这个例子似乎是模板函数的半特化，c++11以前是不支持的*）。模板半特化的方式优于重载的方式在于重载可能需要很多种的重载实现，并且大部分可能重复。

```
template <typename T>
void foo_impl (const T& val, std::true_type)
{
  std::cout <<"calls for a pointer" <<std::endl;
}

template <typename T>
void foo_impl (const T& val, std::false_type)
{
  std::cout <<"calls for a value" <<std::endl;
}

template <typename T>
void foo (const T& val)
{
  foo_impl(val, std::is_pointer<T>());
}
```

## Type Traits的分类

1） 类型判断，返回std::true或者std::false

```
is_void<T>
is_integral<T>
...
```

2）类型关系，返回std::true或者std::false

```
is_same<T1, T2>
is_base_of<T, D>
...
```

3）类型修改

```
typedef int T;
add_const<T>::type            // const int
add_lvalue_reference<T>::type // int&
add_rvalue_reference<T>::type // int&&
```

4）其他类型

```
rank<T>
common_type<T1, ...>
...
```

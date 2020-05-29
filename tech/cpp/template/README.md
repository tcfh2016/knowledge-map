# 模板基础

## 模板的使用

## 模板实例化

## 常见的问题

### 1.为什么模板的定义要在头文件中？

在进行模板实例化时，编译器需要知道模板的定义，这不同于普通函数编译和链接的区别。普通函数在编译的时候只需要函数的声明（定义不必须），但时模板就不可易，因此模板的定义通常都是放在头文件中的。

### 2.模板的实例化、特化

模板的实例化是编译器根据特定类型隐式/显示地生成对应版本的函数或者类，这个过程是实例化。而特化则是我们需要动手将已有的模板进行自定义：

- 全特化，所有的模板参数都是明确的类型。*类模板和函数模板均适用。*
- 偏特化/局部特化，部分模板参数是明确的类型。*仅类模板适用。*

如下的示例是类模板的特化：

```
// 类模板
template <class T1, class T2>
class A{
    T1 data1;
    T2 data2;
};

// 全特化类模板
template <>
class A<int, double>{
    int data1;
    double data2;
};

// 偏特化类模板
template <class T2>
class A<int, T2>{
    ...
};
```

如下的示例是函数模板的特化：

```
// 函数模板
template <class T>
T max(const T lhs, const T rhs){   
    return lhs > rhs ? lhs : rhs;
}

// 全特化函数模板
template <>
int max(const int lhs, const int rhs){   
    return lhs > rhs ? lhs : rhs;
}

// 偏特化函数模板，错误。
template <class T2>
void f<int, T2>(){}
```

参考：

- [C++模板的偏特化与全特化](https://harttle.land/2015/10/03/cpp-template.html)
- [函数模板的特化和重载](https://imzlp.me/posts/10380/)

### 3.函数模板的特化和函数重载的区别？

函数模板的特化和重载函数功能是没有太大的区别，但是两者的签名规则是不同的。是无法进行

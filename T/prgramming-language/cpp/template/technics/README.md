## 关键字 typename

`typename`除了具有与`class`微小的区别外，还可以用来在模板内部作为标识符来标识类型，比如：

```
template <typename T>
class MyClass
{
  typename T::SubType* ptr;
  ...
}
```

如果没有`typename`在这里，那么`T::SubType`会被识别为一个静态的成员，`T::SubType * ptr`会被认为是两个变量的乘积。有了typename编译器就能够知道SubType是定义在T内部的一种类型。

## .template构造

在《C++ Template》里面是按照`.template`这么讲解，但从[.template (dot-template) construction usage [duplicate]](https://stackoverflow.com/questions/8463368/template-dot-template-construction-usage)有人指出合理的解释应该是`.` + `template`，`template`关键字主要用来修饰后面跟着的成员函数，表明该成员函数是一个“函数模板”。

```
template <int N>
class MyIntContainer
{
public:
  template <int I>
  int getValue() const
  {
    return data[I];
  }
private:
  int data[N];
};

template <int N, int I>
void print(MyIntContainer<N> const& mc)
{
  std::cout <<mc. template getValue<I>() <<std::endl;
}
```

上面的代码语句`std::cout <<mc. template getValue<I>() <<std::endl;`如果没有`template`显示指明`getValue<I>()`是函数模板那么编译会出错。

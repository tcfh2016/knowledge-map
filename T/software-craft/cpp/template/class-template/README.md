## 类模板的声明

函数模板定义的时候需要指定“模板参数”和“调用参数”，类模板在定义的时候简单一点，仅需要指定模板参数即可。

```
template <typename T>
class Stack{
  ...
};
```


## 成员函数的实现

成员函数的实现如果定义在类声明里，如果放在外面那么需要将该成员函数定义为模板函数并且还需要使用类模板的完整类型限定符（即`Stack<T>::`）：

```
template <typename T>
class Stack{
  ...
  void push(T const& elem)
  {
    ...
  }
};

// 定义在类声明之外
template <typename T>
void Stack<T>::push (T const& elem)
{
  ...
}
```


## 类模板的使用

使用类模板的时候需要显示指定模板实参，比如`Stack<int>  intStack`。注意，只有那些被调用的成员函数，才会产生这些函数的实例化代码。


## 类模板的特化

和函数模板的重载类似，可以通过模板实参来特化类模板，从而优化基于某种特定类型的实现或者克服某种特定类型在实例化类模板时所表现的不足（比如没有提供某种操作）。特别类模板的操作是在起始处声明`template<>`，然后还需要特化该类模板的所有成员函数：

```
template<>
class Stack<std::string>
{
  ...
  void push(T const& elem)
  {
    ...
  }
}

// 定义在类声明之外
void Stack<std::string>::push (std::string const& elem)
{
  ...
}
```


## 类模板的局部特化/偏特化

当有多个模板参数的时候，类模板可以进行局部特化，比如：

```
template <typename T1, typename T2>
class MyClass
{

}

template <typename T>
class MyClass<T, int>
{

}
```

## 缺省模板实参

```
template <typename T, typename CONT = std::vector<T>>
class Stack
{
  CONT elems;
  void push(T const&)
  {
    ...
  }
}
```

既可以`Stack<int> intStack`，又可以`Stack<double, std::deque<double>> doubleStack`。


## 非类型模板参数

模板参数不局限于类型，也可以将普通值作为模板参数。在使用的时候可以通过`Stack<int, 20> int20Stack;`来进行实例化。

```
template <typename T, int MAXSIZE>
class Stack
{
  T elems[MAXSIZE];
}
```

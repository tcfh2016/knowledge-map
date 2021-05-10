## 构造器

### [Copy构造器](https://en.cppreference.com/w/cpp/language/copy_constructor)

拷贝构造器是在使用一个老的对象去构造新的对象的时候调用的，常见的场景存在于：1）初始化，比如`T a = b;`或者`T a(b)`；2）对象作为函数参数值传递，比如`f(a)`(函数f的声明为`void f(T t)`)；3）在函数中作为返回值返回的时候。

共有如下几种语法：

```
class_name (const class_name &); // 自定义拷贝构造器
class_name (const class_name &) = default; // 让编译起生成默认拷贝构造器
class_name (const class_name &) = delete; // 禁止拷贝构造器的默认生成
```

### [Move构造器](https://en.cppreference.com/w/cpp/language/move_constructor)

移动构造器是c++11的新生事物，在geeksforgeeks网站上有篇[文章](https://www.geeksforgeeks.org/move-constructors-in-c-with-examples/)为此有很详细的说明，之所以有这个Move构造器是为了优化构造器的多次调用以及Copy构造器对于内存的深拷贝。

简单来说，Move构造器的使用会减少构造器调用次数（避免多次创建临时对象），同时在Move构造器内部也不是像Copy构造器那样执行对象之间的深度拷贝，对于构造器中涉及到内存的拷贝，Move构造器所做的工作仅仅是将指针指向老的对象，同时将老对象指针置为无效值。

Move构造器的定义和使用场景和Copy构造器类似，只不过在语法和使用语义上有些不同。

```
class_name (const class_name &&);
class_name (const class_name &&) = default;
class_name (const class_name &&) = delete;
```

## error: member access into incomplete type

- [https://stackoverflow.com/questions/19962812/error-member-access-into-incomplete-type-forward-declaration-of](https://stackoverflow.com/questions/19962812/error-member-access-into-incomplete-type-forward-declaration-of)

## 类定义里面无法创建对象进行初始化

好久没写代码，秀逗了。

```
class Mocker
{
  Mocker(int i)  {}
  ~Mocker()  {}
  ...
}

class Container
{
  Mocker mocker(1);
}
```

正确写法：

```
class Mocker
{
  Mocker(int i)  {}
  ~Mocker()  {}
  ...
}

class Container
{
  Container():mocker(1){}

  Mocker mocker;
}
```

## Q&A

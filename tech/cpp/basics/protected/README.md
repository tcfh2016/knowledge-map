在之前的C++的编程实践中很少使用到 `protected`关键字，对于它本身所蕴含的概念逐渐生疏。它
的使用常在于修饰成员变量和继承。

# protected 成员

按照语法定义，`protected`表示继承时子类可以对基类有完全访问权，在《大话设计模式》里有这
样一个例子很好的说明了它的使用场景。

```
class Animal
{
protected:
  std::string _name;  // 该属性主要是为派生类所用，因此可以声明为`protected`。
  int _shoutNum;

public:
  Animal(std::string name):_shoutNum(3)
  {
    _name = name;
  }

  Animal():_shoutNum(3)
  {
    _name = "unknown";
  }

  std::string getName()
  {
    return _name;
  }

  int getShoutNum()
  {
    return _shoutNum;
  }

  void setShoutNum(int value)
  {
    _shoutNum = value;
  }
};

class Cat : public Animal
{
public:
  Cat():Animal() {}
  Cat(std::string name):Animal(name){} // 派生类中针对基类的初始化。

  std::string shout()
  {
    std::string res = "";
    for (int i = 0; i <_shoutNum; ++i)
    {
      res += "miao ";
    }
    return (_name + ": " + res);
  }
};
```

*注：派生类构造函数同样是通过构造函数初始化列表来将实参传递给基类构造函数。*


# protected 继承

protected 继承不常用，它的出现经常见于与 private继承、public继承之区别的讨论当中：

- public继承体现出父子类之间的"is-a”关系。
- private继承意味着 “Implemented-in-terms-of”，即继承父类的实现。
- protected继承类似于private继承，但是极少使用。

《Effective C++》的作者Soctt Meyers在“条款32”里也提到protected继承是一直困惑它的东西。

即便如此，我们可以从如下简易代码学习并了解`protected`, `private`,`public`在修饰成员及
继承时候的区别(StackOverflow问答[Difference between private, public, and protected inheritance]())

```
class A
{
public:
    int x;
protected:
    int y;
private:
    int z;
};

class B : public A
{
    // x is public
    // y is protected
    // z is not accessible from B
};

class C : protected A
{
    // x is protected
    // y is protected
    // z is not accessible from C
};

class D : private A    // 'private' is default for classes
{
    // x is private
    // y is private
    // z is not accessible from D
};
```

# 参考

- [Difference between private, public, and protected inheritance](https://stackoverflow.com/questions/860339/difference-between-private-public-and-protected-inheritance)
- [Why do we actually need Private or Protected inheritance in C++?](https://stackoverflow.com/questions/374399/why-do-we-actually-need-private-or-protected-inheritance-in-c/374423#374423)

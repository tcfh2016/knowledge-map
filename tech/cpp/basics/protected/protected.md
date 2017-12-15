在之前的C++的编程实践中很少使用到 `protected`关键字，对于它本身所蕴含的概念逐渐生疏。今
天阅读《大话设计模式》的时候突然看到一个例子，很好的说明了它的使用场景。

按照语法定义，`protected`表示继承时子类可以对基类有完全访问权。

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

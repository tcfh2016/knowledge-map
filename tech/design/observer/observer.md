
2017年10月23日16:35:07
先仿照示例写了一个交叉引用的观察者原型（`参考coupled_version.cpp`)，却碰到交叉引用造就的编译问题：

```
[lianbche@hzlinb17 observer]$ g++ coupled_version.cpp -o coupled_version
coupled_version.cpp:24: error: field ‘_secretary’ has incomplete type
coupled_version.cpp: In constructor ‘StockObserver::StockObserver(std::string, Secretary)’:
coupled_version.cpp:10: error: ‘secretary’ has incomplete type
coupled_version.cpp:5: error: forward declaration of ‘struct Secretary’
coupled_version.cpp:13: error: ‘_secretary’ was not declared in this scope
coupled_version.cpp: In member function ‘void StockObserver::update()’:
coupled_version.cpp:19: error: ‘_secretary’ was not declared in this scope
[lianbche@hzlinb17 observer]$
```

尝试着使用前置声明来解决该问题，但没有办法办到：因为每个类的成员方法中均相互调用它所交叉
引用的类，这是前置声明无法办到的事。而弥补的方法在于将前一个版本分离。
*注：前向声明的作用类型是不完全类型，它只能以有限方式使用：① 不能定义该类型的对象，仅用于
定义指向该类型的指针及引用；②用于声明(而不是定义)使用该类型作为形参类型或返回类型的函数。*

```
#include <iostream>
#include <list>

//class StockObserver;
class Secretary;

class StockObserver
{
public:
  StockObserver(std::string name, Secretary secretary)
  {
    _name = name;
    _secretary = secretary;
  }
  ~StockObserver(){}

  void update()
  {
    std::cout <<_secretary.getAction() <<_name <<" close stock windows, keep on working." <<std::endl;
  }

private:
  std::string _name;
  Secretary _secretary;
};  

class Secretary
{
public:
  Secretary(){}
  ~Secretary(){}

  void attach(StockObserver observer)
  {
    _observers.push_back(observer);
  }

  void notify()
  {
    for (std::list<StockObserver>::iterator iter = _observers.begin();
      iter != _observers.end();
      ++iter)
    {
      iter->update();
    }
  }

  std::string setAction(std::string action)
  {
    _action = action;
  }

  std::string getAction()
  {
    return _action;
  }

private:
  std::string _action;
  std::list<StockObserver> _observers;
};


int main()
{
  Secretary *s = new Secretary();
  StockObserver *t1 = new StockObserver("App", *s);
  StockObserver *t2 = new StockObserver("Bpp", *s);

  s->setAction("Boss is coming.");
  s->notify();

  return 0;
}
```

讨论C++前向声明的一个问答：
https://www.zhihu.com/question/63201378

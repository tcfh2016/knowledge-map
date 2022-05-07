## 继承

## 虚拟继承

C++中的多态是通过虚继承特性来实现的，比如如下的`DarkRoas`继承自`Beverage`：

```
class Beverage {

public:
  Beverage(){}
  virtual std::string getDescription() {return "description";}
  virtual double getCost() {return 0.0;}
};

class DarkRoast : public Beverage {

public:
  DarkRoast(){}
  std::string getDescription() {return "DarkRoast";}
  double getCost() {return 0.99;}
};
```

但多态性必须要通过指针或者引用进行访问才能够体现出来：

```
Beverage *beverage = new DarkRoast();
std::cout <<"book: " <<beverage->getDescription() <<std::endl;
std::cout <<"cost: " <<beverage->getCost() <<std::endl;

auto k = *beverage;
std::cout <<"book: " <<k.getDescription() <<std::endl;
std::cout <<"cost: " <<k.getCost() <<std::endl;
```

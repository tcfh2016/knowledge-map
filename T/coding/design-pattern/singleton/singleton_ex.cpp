#include <iostream>

class Singleton{

public:
  static Singleton* getInstance()
  {
    if (uniqueInstance == nullptr)
    {
      uniqueInstance = new Singleton();
    }
    return uniqueInstance;
  }

private:
  static Singleton* uniqueInstance;
  Singleton(){}
};

Singleton* Singleton::uniqueInstance = nullptr;

int main()
{
  Singleton *instance1 = Singleton::getInstance();
  std::cout <<"address of instance1" <<instance1 <<std::endl;
  Singleton *instance2 = Singleton::getInstance();
  std::cout <<"address of instance1" <<instance2 <<std::endl;
}

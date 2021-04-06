#include <iostream>

class Animal
{
protected:
  std::string _name;
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
  Cat(std::string name):Animal(name){}

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

int main()
{
  Cat cat("MIMI");
  std::cout <<cat.shout() <<std::endl;

  return 0;
}

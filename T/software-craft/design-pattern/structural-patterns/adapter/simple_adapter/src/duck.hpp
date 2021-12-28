#pragma once
#include <iostream>

class Duck {
public:
  virtual void quack() = 0;
  virtual void fly() = 0;
};

class MallardDuck : public Duck {
public:
  void quack() {
    std::cout <<"Mallard quck quack" <<std::endl;
  }
  void fly() {
    std::cout <<"Mallark duck is flying..." <<std::endl;
  }
};

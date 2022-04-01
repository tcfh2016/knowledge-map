#pragma once
#include <iostream>

class Turkey {
public:
  virtual void gobble() = 0;
  virtual void fly() = 0;
};

class WildTurkey : public Turkey {
public:
  void gobble() {
    std::cout <<"Wild Turkey gobble" <<std::endl;
  }
  void fly() {
    std::cout <<"Wild Turkey is flying..." <<std::endl;
  }
};

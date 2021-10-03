#pragma once
#include <iostream>

class Light {
public:
  void on() {
    std::cout <<"light on" <<std::endl;
  }
};

class GarageDoor {
public:
  void open() {
    std::cout <<"garage door open" <<std::endl;
  }
};

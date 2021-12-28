#pragma once
#include <iostream>

class Light {
public:
  void on() {
    std::cout <<"light on" <<std::endl;
  }
  void off() {
    std::cout <<"light off" <<std::endl;
  }
};

class GarageDoor {
public:
  void open() {
    std::cout <<"garage door open" <<std::endl;
  }
  void close() {
    std::cout <<"garage door close" <<std::endl;
  }
};

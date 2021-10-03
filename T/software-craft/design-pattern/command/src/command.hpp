#pragma once
#include <iostream>

class Command {
public:
  virtual void execute() = 0;
};

class LightOnCommand : public Command {
public:
  LightOnCommand() {
    std::cout <<"light object attached." <<std::endl;
  }
  void execute() {
    std::cout << "light on" <<std::endl;
  }
private:
  // TODO
};

class GarageDoorOpenCommand : public Command {
public:
  GarageDoorOpenCommand() {
    std::cout <<"garage door object attached." <<std::endl;
  }
  void execute() {
    std::cout << "garage door open" <<std::endl;
  }
private:
  // TODO
};

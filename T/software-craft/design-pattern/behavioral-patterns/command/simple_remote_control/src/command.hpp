#pragma once
#include "appliances.hpp"

class Command {
public:
  virtual void execute() = 0;
};

class LightOnCommand : public Command {
public:
  LightOnCommand(Light *light) {
    _light = light;
  }
  void execute() {
    _light->on();
  }
private:
  Light *_light{nullptr};
};

class GarageDoorOpenCommand : public Command {
public:
  GarageDoorOpenCommand(GarageDoor* garageDoor) {
    _garageDoor = garageDoor;
  }
  void execute() {
    _garageDoor->open();
  }
private:
  GarageDoor *_garageDoor{nullptr};
};

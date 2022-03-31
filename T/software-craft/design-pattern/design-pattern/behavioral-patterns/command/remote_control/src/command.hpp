#pragma once
#include <string>
#include "appliances.hpp"


class Command {
public:
  virtual void execute() {};
  virtual void undo() {};
  virtual std::string getName() { return ""; };
};

class LightOnCommand : public Command {
public:
  LightOnCommand(Light *light):name("LightOnCommand") {
    _light = light;
  }
  void execute() {
    _light->on();
  }
  void undo() {
    _light->off();
  }
  std::string getName() {
    return name;
  }
private:
  std::string name{};
  Light *_light{nullptr};
};


class LightOffCommand : public Command {
public:
  LightOffCommand(Light *light):name("LightOffCommand") {
    _light = light;
  }
  void execute() {
    _light->off();
  }
  void undo() {
    _light->on();
  }
  std::string getName() {
    return name;
  }
private:
  std::string name{};
  Light *_light{nullptr};
};

class GarageDoorOpenCommand : public Command {
public:
  GarageDoorOpenCommand(GarageDoor* garageDoor):name("GarageDoorOpenCommand") {
    _garageDoor = garageDoor;
  }
  void execute() {
    _garageDoor->open();
  }
  void undo() {
    _garageDoor->close();
  }
  std::string getName() {
    return name;
  }

private:
  std::string name{};
  GarageDoor *_garageDoor{nullptr};
};

class GarageDoorCloseCommand : public Command {
public:
  GarageDoorCloseCommand(GarageDoor* garageDoor):name("GarageDoorCloseCommand") {
    _garageDoor = garageDoor;
  }
  void execute() {
    _garageDoor->close();
  }
  void undo() {
    _garageDoor->open();
  }
  std::string getName() {
    return name;
  }

private:
  std::string name{};
  GarageDoor *_garageDoor{nullptr};
};

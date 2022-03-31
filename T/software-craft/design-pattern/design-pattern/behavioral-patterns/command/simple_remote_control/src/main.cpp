#include "remote_control.hpp"
#include "appliances.hpp"

int main()
{
  RemoteControl *rc = new RemoteControl();

  Light* light = new Light();
  LightOnCommand *lightOn = new LightOnCommand(light);
  rc->setCommand(lightOn);
  rc->pressButton();

  GarageDoor* garageDoor = new GarageDoor();
  GarageDoorOpenCommand *doorOpen = new GarageDoorOpenCommand(garageDoor);
  rc->setCommand(doorOpen);
  rc->pressButton();

  return 0;
}

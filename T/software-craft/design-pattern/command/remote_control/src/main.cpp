#include "remote_control.hpp"
#include "appliances.hpp"

int main()
{
  Light* light = new Light();
  LightOnCommand *lightOn = new LightOnCommand(light);
  LightOffCommand *lightOff = new LightOffCommand(light);

  GarageDoor* garageDoor = new GarageDoor();
  GarageDoorOpenCommand *doorOpen = new GarageDoorOpenCommand(garageDoor);
  GarageDoorCloseCommand *doorClose = new GarageDoorCloseCommand(garageDoor);

  RemoteControl *rc = new RemoteControl();
  rc->setCommand(0, lightOn, lightOff);
  rc->setCommand(1, doorOpen, doorClose);
  std::cout <<rc->toString() <<std::endl;

  rc->pressOnButton(0);
  rc->pressUndoButton();
  rc->pressOnButton(1);
  rc->pressOffButton(0);
  rc->pressOffButton(1);

  return 0;
}

#include "remote_control.hpp"

int main()
{
  RemoteControl *rc = new RemoteControl();

  LightOnCommand *lightOn = new LightOnCommand();
  rc->setCommand(lightOn);
  rc->pressButton();

  GarageDoorOpenCommand *doorOpen = new GarageDoorOpenCommand();
  rc->setCommand(doorOpen);
  rc->pressButton();

  return 0;
}

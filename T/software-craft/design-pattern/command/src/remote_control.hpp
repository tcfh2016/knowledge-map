#include "command.hpp"

class RemoteControl {
public:
    RemoteControl(){}
    void setCommand(Command *command) {
      slot = command;
    }
    void pressButton() {
      slot->execute();
    }
private:
    Command *slot{nullptr};
};

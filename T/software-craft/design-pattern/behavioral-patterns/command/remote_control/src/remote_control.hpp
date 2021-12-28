#include "command.hpp"
#include <array>
#include <sstream>
#include <string>

class RemoteControl {
  static const int SlotSize = 7;

public:
    RemoteControl() {
      Command* noCommand = new Command();
      for (auto i = 0; i < SlotSize; ++i) {
        onCommands.at(i) = noCommand;
        offCommands.at(i) = noCommand;
      }
      undoCommand = noCommand;
    }
    void setCommand(int slot, Command* onCommand, Command* offCommand) {
      onCommands.at(slot) = onCommand;
      offCommands.at(slot) = offCommand;
    }

    void pressOnButton(int slot) {
      onCommands.at(slot)->execute();
      undoCommand = onCommands.at(slot);
    }

    void pressOffButton(int slot) {
      offCommands.at(slot)->execute();
      undoCommand = offCommands.at(slot);
    }

    void pressUndoButton() {
      undoCommand->undo();
    }

    std::string toString() {
      std::ostringstream os;
      os <<"\n------Remote Control------\n";
      for (auto i = 0; i < SlotSize; ++i) {
        os <<"slot[" << i << "] " <<onCommands.at(i)->getName() <<" " <<offCommands.at(i)->getName() <<"\n";
      }
      return os.str();
    }

private:
    std::array<Command*, SlotSize> onCommands;
    std::array<Command*, SlotSize> offCommands;
    Command* undoCommand;
};

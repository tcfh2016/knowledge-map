#include <iostream>
#include "diner_menu.hpp"
#include "pancake_house_menu.hpp"

void printMenu(Iterator* iterator) {
  while (iterator->hasNext()) {
    auto& item = iterator->next();
    std::cout <<item.getName() <<" " <<item.getPrice() <<" "<<item.getDescription() <<std::endl;
  }
}

int main() {
  PancakeHouseMenu* pancakeHouseMenu = new PancakeHouseMenu();
  auto& breakfastItems = pancakeHouseMenu->getMenuItems();

  DinerMenu* dinerMenu = new DinerMenu();
  auto& lunchItem = dinerMenu->getMenuItems();

  std::cout <<"----------------ITERATE ELEMENT---------------" <<std::endl;
  for (auto item : breakfastItems) {
    std::cout <<item.getName() <<" " <<item.getPrice() <<" "<<item.getDescription() <<std::endl;
  }
  for (auto item : lunchItem) {
    if (item) {
      std::cout <<item->getName() <<" " <<item->getPrice() <<" "<<item->getDescription() <<std::endl;
    }
  }

  std::cout <<"----------------USING ITERATOR----------------" <<std::endl;
  printMenu(pancakeHouseMenu->createIterator());
  printMenu(dinerMenu->createIterator());

  return 0;
}

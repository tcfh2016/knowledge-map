#include <iostream>
#include "diner_menu.hpp"
#include "pancake_house_menu.hpp"

int main() {
  PancakeHouseMenu* pancakeHouseMenu = new PancakeHouseMenu();
  auto& breakfastItems = pancakeHouseMenu->getMenuItems();

  DinerMenu* dinerMenu = new DinerMenu();
  auto& lunchItem = dinerMenu->getMenuItems();

  for (auto item : breakfastItems) {
    std::cout <<item.getName() <<" " <<item.getPrice() <<" "<<item.getDescription() <<std::endl;
  }

  for (auto item : lunchItem) {
    std::cout <<item->getName() <<" " <<item->getPrice() <<" "<<item->getDescription() <<std::endl;
  }
  return 0;
}

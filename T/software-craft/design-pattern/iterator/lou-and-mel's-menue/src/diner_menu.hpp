#pragma once
#include <iostream>
#include <array>
#include <string>
#include "menu_item.hpp"

class DinerMenu {
public:
  static const int MAX_ITEMS = 6;

public:
  DinerMenu() {
    addItem("Vegetarian BLT", "Fakin Bacon with lettuce&tomato on whole wheat", true, 2.99);
    addItem("BLT", "Bacon with lettuce&tomato on whole wheat", false, 2.99);
    addItem("Soup of the day", "Soup of the day, with a side of potato salad", false, 3.29);
    addItem("Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", false, 3.05);
  }

  void addItem(std::string name, std::string description, bool vegetarian, double price) {
    if (numberOfItems >= MAX_ITEMS) {
      std::cout <<"Sorry, menue is full!" <<std::endl;
    }
    else {
      menuItems[numberOfItems++] = new MenuItem(name, description, vegetarian, price);
    }
  }

  std::array<MenuItem*, MAX_ITEMS>& getMenuItems() {
    return menuItems;
  }

private:
  int numberOfItems{0};
  std::array<MenuItem*, MAX_ITEMS> menuItems;
};

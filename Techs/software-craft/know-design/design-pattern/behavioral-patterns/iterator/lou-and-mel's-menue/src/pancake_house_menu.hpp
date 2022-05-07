#pragma
#include <list>
#include <string>
#include "menu_item.hpp"

class PancakeHouseMenu {
  class PancakeHouseMenuIterator : public Iterator {
  public:
    PancakeHouseMenuIterator(std::list<MenuItem>& itemList):
      _itemList(itemList),
      _curPosition(itemList.begin()) {
    }

    bool hasNext() {
      if (_curPosition != _itemList.end()) {
        return true;
      }
      else {
        return false;
      }
    }

    MenuItem& next() {
      return *_curPosition++;
    }
  private:
    std::list<MenuItem>& _itemList;
    std::list<MenuItem>::iterator _curPosition;
  };

public:
  PancakeHouseMenu() {
    addItem("K&B Pancake Breakfast", "Pancake with scrambled eggs, and toast", true, 2.99);
    addItem("Regular Pancake Breakfast", "Pancake with fried eggs, sausage", false, 2.99);
    addItem("Blueberry Pancakes", "Pancake made with fresh blueberries", true, 3.49);
    addItem("Waffles", "Waffles, with your choice of blueberries or strawberries", true, 3.59);
  }

  void addItem(std::string name, std::string description, bool vegetarian, double price) {
    MenuItem item(name, description, vegetarian, price);
    itemList.push_back(item);
  }

  std::list<MenuItem>& getMenuItems() {
    return itemList;
  }

  Iterator* createIterator() {
    return new PancakeHouseMenuIterator(itemList);
  }

private:
  std::list<MenuItem> itemList;
};

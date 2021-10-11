#pragma once
#include <string>

class MenuItem {
public:
  MenuItem(std::string& name,
           std::string& description,
           bool vegetarian,
           double price)  {
    _name = name;
    _description = description;
    _vegetarian = vegetarian;
    _price = price;
  }

  std::string getName() {
    return _name;
  }

  std::string getDescription() {
    return _description;
  }

  double getPrice() {
    return _price;
  }

  bool isVegetarian() {
    return _vegetarian;
  }

private:
  std::string _name;
  std::string _description;
  bool _vegetarian;
  double _price;
};

class Iterator {
public:
  virtual bool hasNext() = 0;
  virtual MenuItem& next() = 0;
};

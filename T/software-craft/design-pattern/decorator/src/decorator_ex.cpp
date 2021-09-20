#include <iostream>
#include <string>

class Beverage {
  std::string description;
  double cost;

public:
  std::string getDescription() {return description;}
  double getCost() {return cost;}
};

class HouseBlend : public Beverage {

};

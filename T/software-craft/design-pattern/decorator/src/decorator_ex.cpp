#include <iostream>
#include <string>

class Beverage {

public:
  Beverage(){}
  virtual std::string getDescription() {return "description";}
  virtual double getCost() {return 0.0;}
};

// Different kinds of coffee
class HouseBlend : public Beverage {

public:
  HouseBlend(){}
  std::string getDescription() {return "House Blend Coffee";}
  double getCost() {return 0.89;}
};

class DarkRoast : public Beverage {

public:
  DarkRoast(){}
  std::string getDescription() {return "DarkRoast";}
  double getCost() {return 0.99;}
};

class Espresso : public Beverage {

public:
  Espresso(){}
  std::string getDescription() {return "Espresso";}
  double getCost() {return 1.99;}
};

class Decaf : public Beverage {

public:
  Decaf(){}
  std::string getDescription() {return "Decaf";}
  double getCost() {return 1.05;}
};

// Different kinds of condiments
class CondimentDecorator : public Beverage {

public:
  CondimentDecorator(){}
  std::string getDescription() {return "";}
};

class Milk : public CondimentDecorator {
Beverage* wrappedBeverage;

public:
  Milk(Beverage* obj) { wrappedBeverage = obj; }
  std::string getDescription() {
    return "Milk + " + wrappedBeverage->getDescription();
  }
  double getCost() {
    return 0.0 + wrappedBeverage->getCost();
  }
};

class Mocha : public CondimentDecorator {
Beverage* wrappedBeverage;

public:
  Mocha(Beverage* obj) { wrappedBeverage = obj; }
  std::string getDescription() {
    return "Mocha + " + wrappedBeverage->getDescription();
  }
  double getCost() {
    return 0.20 + wrappedBeverage->getCost();
  }
};

class Soy : public CondimentDecorator {
Beverage* wrappedBeverage;
public:
  Soy(Beverage* obj) { wrappedBeverage = obj; }
  std::string getDescription() {
    return "Soy + " + wrappedBeverage->getDescription();
  }
  double getCost() {
    return 0.0 + wrappedBeverage->getCost();
  }
};

class Whip : public CondimentDecorator {
Beverage* wrappedBeverage;

public:
  Whip(Beverage* obj) { wrappedBeverage = obj; }
  std::string getDescription() {
    return "Whip + " + wrappedBeverage->getDescription();
  }
  double getCost() {
    return 0.10 + wrappedBeverage->getCost();
  }
};

int main()
{
  // book Whip + Mocha + DarkRoast coffee
  Beverage *beverage = new DarkRoast();
  std::cout <<"book: " <<beverage->getDescription() <<std::endl;
  std::cout <<"cost: " <<beverage->getCost() <<std::endl;

  beverage = new Whip(beverage);
  std::cout <<"book: " <<beverage->getDescription() <<std::endl;
  std::cout <<"cost: " <<beverage->getCost() <<std::endl;

  beverage = new Mocha(beverage);
  std::cout <<"book: " <<beverage->getDescription() <<std::endl;
  std::cout <<"cost: " <<beverage->getCost() <<std::endl;

  return 0;
}

#include "pizza_store.hpp"
#include "../pizza/pizza_newyork.hpp"

class NewyorkStylePizzaStore : public PizzaStore {
public:
  virtual Pizza* createPizza(std::string type)
  {
    Pizza* pizza = nullptr;
    if (type == "cheese") {
      pizza = new NYStyleCheesePizza();
    }
    else if (type == "pepperoni") {
      pizza = new NYStylePepperoniPizza();
    }
    else if (type == "clam") {
      pizza = new NYStyleClamPizza();
    }
    else if (type == "veggie") {
      pizza = new NYStyleVeggiePizza();
    }
    else {
      std::cout <<"unknown chicago style pizza!!!" <<std::endl;
    }

    return pizza;
  }
};

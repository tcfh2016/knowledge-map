#include "pizza_store.hpp"
#include "../pizza/pizza_chicago.hpp"

class ChicagoStylePizzaStore : public PizzaStore {
public:
  virtual Pizza* createPizza(std::string type)
  {
    Pizza* pizza = nullptr;
    if (type == "cheese") {
      pizza = new CCStyleCheesePizza();
    }
    else if (type == "pepperoni") {
      pizza = new CCStylePepperoniPizza();
    }
    else if (type == "clam") {
      pizza = new CCStyleClamPizza();
    }
    else if (type == "veggie") {
      pizza = new CCStyleVeggiePizza();
    }
    else {
      std::cout <<"unknown chicago style pizza!!!" <<std::endl;
    }

    return pizza;
  }
};

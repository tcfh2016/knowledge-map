#include <string>
#include "../pizza/pizza.hpp"

class PizzaStore {

public:
  virtual Pizza* createPizza(std::string type){
    return nullptr;
  };
  Pizza* orderPizza(std::string type) {
    Pizza* pizza;

    pizza = createPizza(type);
    pizza->prepare();
    pizza->bake();
    pizza->cut();
    pizza->box();

    return pizza;
  }
};

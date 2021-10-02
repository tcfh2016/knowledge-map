#include <iostream>
#include "pizza.hpp"

class CheesePizza : public Pizza {
public:
  CheesePizza(PizzaIngredientFactory &pizzaIngredientFactory):
    _pizzaIngredientFactory(pizzaIngredientFactory) {

  }
  void prepare() {
    _pizzaIngredientFactory.createDough();
    _pizzaIngredientFactory.createSauce();
  }
private:
  PizzaIngredientFactory &_pizzaIngredientFactory;
};

#include <iostream>
#include "pizza.hpp"

class ClamPizza : public Pizza {
public:
  ClamPizza(PizzaIngredientFactory &pizzaIngredientFactory):
    _pizzaIngredientFactory(pizzaIngredientFactory) {

  }
  void prepare() {
    _pizzaIngredientFactory.createDough();
    _pizzaIngredientFactory.createSauce();
  }
private:
  PizzaIngredientFactory &_pizzaIngredientFactory;
};

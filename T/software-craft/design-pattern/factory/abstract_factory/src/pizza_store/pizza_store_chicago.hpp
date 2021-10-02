#include "pizza_store.hpp"
#include "../pizza_ingredient/pizza_ingredient.hpp"
#include "../pizza/pizza_cheese.hpp"
#include "../pizza/pizza_clam.hpp"

class ChicagoStylePizzaStore : public PizzaStore {
public:
  virtual Pizza* createPizza(std::string type)
  {
    Pizza* pizza = nullptr;
    PizzaIngredientFactory* ingredientFactory = new CCPizzaIngredientFactory();

    if (type == "cheese") {
      pizza = new CheesePizza(*ingredientFactory);
    }
    else if (type == "clam") {
      pizza = new ClamPizza(*ingredientFactory);
    }
    else {
      std::cout <<"unknown chicago style pizza!!!" <<std::endl;
    }

    return pizza;
  }
};

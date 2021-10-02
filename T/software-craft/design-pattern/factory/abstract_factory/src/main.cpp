#include <iostream>
#include "./pizza_store/pizza_store_newyork.hpp"

int main()
{
  // Jim: order one Newyork style cheese pizza
  PizzaStore* nyPizzaStore = new NewyorkStylePizzaStore();
  nyPizzaStore->orderPizza("cheese");

  // Kim: order one Chicago style cheese pizza
}

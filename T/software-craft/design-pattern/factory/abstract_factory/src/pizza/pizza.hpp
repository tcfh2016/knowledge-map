#pragma once
#include "../pizza_ingredient/pizza_ingredient.hpp"

class Pizza {
public:
  virtual void prepare() = 0;

  void bake() {
    std::cout <<"Bake Chicago cheese pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut Chicago cheese pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box Chicago cheese pizza!" <<std::endl;
  }

private:
  Dough *dough{nullptr};
  Sauce *sauce{nullptr};
};

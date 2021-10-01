#include <iostream>
#include "pizza.hpp"

class CCStyleCheesePizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare Chicago cheese pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake Chicago cheese pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut Chicago cheese pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box Chicago cheese pizza!" <<std::endl;
  }
};

class CCStylePepperoniPizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare Chicago pepperoni pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake Chicago pepperoni pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut Chicago pepperoni pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box Chicago pepperoni pizza!" <<std::endl;
  }
};

class CCStyleClamPizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare Chicago clam pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake Chicago clam pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut Chicago clam pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box Chicago clam pizza!" <<std::endl;
  }
};

class CCStyleVeggiePizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare Chicago veggie pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake Chicago veggie pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut Chicago veggie pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box Chicago veggie pizza!" <<std::endl;
  }
};

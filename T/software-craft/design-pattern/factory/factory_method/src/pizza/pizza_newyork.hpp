#include <iostream>
#include "pizza.hpp"

class NYStyleCheesePizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare New York cheese pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake New York cheese pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut New York cheese pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box New York cheese pizza!" <<std::endl;
  }
};

class NYStylePepperoniPizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare New York pepperoni pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake New York pepperoni pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut New York pepperoni pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box New York pepperoni pizza!" <<std::endl;
  }
};

class NYStyleClamPizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare New York clam pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake New York clam pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut New York clam pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box New York clam pizza!" <<std::endl;
  }
};

class NYStyleVeggiePizza : public Pizza {
public:
  void prepare() {
    std::cout <<"Prepare New York veggie pizza!" <<std::endl;
  }

  void bake() {
    std::cout <<"Bake New York veggie pizza!" <<std::endl;
  }

  void cut() {
    std::cout <<"Cut New York veggie pizza!" <<std::endl;
  }

  void box() {
    std::cout <<"Box New York veggie pizza!" <<std::endl;
  }
};

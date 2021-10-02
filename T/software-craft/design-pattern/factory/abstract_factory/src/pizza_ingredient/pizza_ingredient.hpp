#pragma once
#include <iostream>

// Integredient family
class Dough {
  virtual void prepareDough() = 0;
};

class ThinCrustDough : public Dough {
public:
  ThinCrustDough() {
    prepareDough();
  }
  virtual void prepareDough() {
    std::cout <<"prepare thin crust dough!" <<std::endl;
  }
};

class ThickCrustDough : public Dough {
public:
  ThickCrustDough() {
    prepareDough();
  }
  virtual void prepareDough() {
    std::cout <<"prepare thick crust dough!" <<std::endl;
  }
};

class Sauce {
  virtual void prepareSauce() = 0;
};

class MarinaraSauce : public Sauce {
public:
  MarinaraSauce() {
    prepareSauce();
  }
  virtual void prepareSauce() {
    std::cout <<"prepare marinara sauce!" <<std::endl;
  }
};

class PlumTomatoSauce : public Sauce {
public:
  PlumTomatoSauce() {
    prepareSauce();
  }
  virtual void prepareSauce() {
    std::cout <<"prepare plum tomato sauce!" <<std::endl;
  }
};


// Ingredient factory

class PizzaIngredientFactory {
public:
  virtual Dough* createDough() = 0;
  virtual Sauce* createSauce() = 0;
};

class NYPizzaIngredientFactory : public PizzaIngredientFactory {
public:
  virtual Dough* createDough() {
    return new ThinCrustDough();
  }

  virtual Sauce* createSauce() {
    return new MarinaraSauce();
  }
};

class CCPizzaIngredientFactory : public PizzaIngredientFactory {
public:
  virtual Dough* createDough() {
    return new ThickCrustDough();
  }

  virtual Sauce* createSauce() {
    return new PlumTomatoSauce();
  }
};

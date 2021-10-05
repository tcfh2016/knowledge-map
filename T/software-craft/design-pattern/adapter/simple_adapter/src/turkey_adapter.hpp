#pragma once
#include "duck.hpp"
#include "turkey.hpp"


class TurkeyAdapter : public Duck {
public:
  TurkeyAdapter(Turkey* turkey) {
    _turkey = turkey;
  }

  void quack() {
    _turkey->gobble();
  }

  void fly() {
    _turkey->fly();
  }

private:
  Turkey* _turkey{nullptr};
};

#include <iostream>

int main() {
  // simple lambda definition.
  [] {
    std::cout <<"I'm the first simple lambda expression!" <<std::endl;
  };

  // simple lambda definition and calling.
  [] {
    std::cout <<"I'm the second simple lambda expression!" <<std::endl;
  }();

  // assign the lambda expression to one variable.
  auto l = [] {
    std::cout <<"I'm the third simple lambda expression!" <<std::endl;
  };
  l();

  return 0;
}

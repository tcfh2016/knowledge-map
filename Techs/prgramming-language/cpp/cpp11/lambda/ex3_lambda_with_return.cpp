#include <iostream>

int main() {

  auto l1 = [] {
    return 99.99;
  };
  std::cout <<l1() << std::endl;

  auto l2 = []() -> int {
    return 99.99;
  };
  std::cout <<l2() << std::endl;

  return 0;
}

#include <iostream>

int main() {
  int x = 0;

  auto e = [x]() mutable {
    std::cout <<x << std::endl;
    ++x;
  };

  x = 100;
  e();
  e();
  std::cout <<x << std::endl;

  return 0;
}

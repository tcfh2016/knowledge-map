#include <iostream>

int main() {
  int x = 0;
  int y = 0;

  auto e = [&] {
    std::cout <<x+y << std::endl;
    ++y;
  };

  e();
  e();

  return 0;
}

#include <iostream>

int main() {
  // lambda with parameter passed by value.
  auto la = [](int x) {
    std::cout <<x <<std::endl;
    x = 200;
  };

  auto a = 100;
  la(a);
  la(a);

  // lambda with parameter passed by reference.
  auto la_r = [](int& x) {
    std::cout <<x <<std::endl;
    x = 200;
  };

  auto b = 100;
  la_r(b);
  la_r(b);

  return 0;
}

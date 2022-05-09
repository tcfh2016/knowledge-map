#include <iostream>

int main() {
  int x = 0;
  int y = 0;

  // 按引用捕获
  auto e = [&] {
    std::cout <<x+y << std::endl;
    ++y;
  };

  e();
  e();

  int a = 0;
  int b = 1;
  auto l = [a, &b] {
    std::cout <<"a = " <<a << std::endl;
    std::cout <<"b = " <<b << std::endl;
    ++b;
  };
  a = 99;
  b = 99;
  l();
  l();
  return 0;
}

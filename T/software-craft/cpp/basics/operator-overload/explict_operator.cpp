#include <iostream>

class T
{
public:
    explicit T(int l, int u) : lower(l), upper(u) {}
    explicit operator int() const { return lower; }

    int lower;
    int upper;
};

int main()
{
  T t(100, 200);
  std::cout <<t.lower <<"," <<t.upper <<std::endl;

  //auto a(t); compiling error
  int a(t);
  std::cout <<a <<std::endl;

  auto b = int(t);
  std::cout <<b <<std::endl;

  auto c = static_cast<int>(t);
  std::cout <<c <<std::endl;

  //auto d = static_cast<long>(t); compiling error
  //std::cout <<d <<std::endl;

  return 0;
}

#include <iostream>
#include <array>

template<class Os, class V>
Os& operator<<(Os& os, const V& v)
{
    os << "{";
    for (auto i : v) os << ' ' << i;
    return os << " } ";
}

int main()
{
  std::array<int, 2> arr1{1,2};
  std::array<int, 2> arr2{3,4};

  auto ref1 = arr1.begin();
  //auto ref2 = arr2.begin();
  std::cout <<arr1 <<arr2 <<*ref1 <<std::endl;
  arr1.swap(arr2);
  std::cout <<arr1 <<arr2 <<*ref1 <<std::endl;

  return 0;
}

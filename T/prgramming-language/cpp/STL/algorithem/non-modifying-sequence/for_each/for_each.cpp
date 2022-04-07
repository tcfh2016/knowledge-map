#include <iostream>
#include <vector>
#include <algorithm>

template <typename T>
void print(const T& t)
{
  for (auto e : t)
  {
    std::cout <<e <<",";
  }
  std::cout <<std::endl;
}

void square(int& e)
{
  e = e * e;
}

int main()
{
  std::vector<int> vec = {1, 2, 3, 4, 5, 6};
  print(vec);

  for_each(vec.begin(), vec.end(), square);
  print(vec);

  for(auto& e: vec)
  {
    e = e*e;
  }
  print(vec);

  return 0;
}

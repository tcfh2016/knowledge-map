#include <iostream>
#include <bitset>

template <int N>
class MyIntContainer
{
public:
  template <int I>
  int getValue() const
  {
    return data[I];
  }
private:
  int data[N];
};

template <int N, int I>
void print(MyIntContainer<N> const& mc)
{
  std::cout <<mc. template getValue<I>() <<std::endl;
}

int main()
{
  MyIntContainer<100> myContainer;
  print<100, 2>(myContainer);
}

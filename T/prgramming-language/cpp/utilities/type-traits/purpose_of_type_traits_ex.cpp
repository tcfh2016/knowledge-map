#include <iostream>

template <typename T>
void foo1 (const T& val)
{
  if (std::is_pointer<T>::value) {
    std::cout <<"calls for a pointer" <<std::endl;
  }
  else {
    std::cout <<"calls for a value" <<std::endl;
  }
}

template <typename T>
void foo_impl (const T& val, std::true_type)
{
  std::cout <<"calls for a pointer" <<std::endl;
}

template <typename T>
void foo_impl (const T& val, std::false_type)
{
  std::cout <<"calls for a value" <<std::endl;
}

template <typename T>
void foo2 (const T& val)
{
  foo_impl(val, std::is_pointer<T>());
}

int main()
{
  int *i = nullptr;
  foo1(i);
  foo2(i);

  return 0;
}

#include <iostream>

template <typename T>
class A {
public:
  A():value_a(100) {}
  ~A(){value_a = 0;}

  T get_A() {
    return value_a;
  }
private:
  T value_a;
};

template <typename T>
class B : public A<T> {
public:
  B():A<T>(),value_b(200) {}
  ~B(){value_b = 0;}

  T get_B() {
    return value_b;
  }
private:
  T value_b;
};

int main() {
  B<int> b;
  std::cout <<b.get_A() <<" " <<b.get_B() <<std::endl;
  return 0;
}

#include <iostream>

template<typename T>
class AutoPointer {
public:
  AutoPointer(T *ptr = nullptr) : pointer(ptr) {
    //
  }
  template<typename U>
  AutoPointer(AutoPointer<U> &rhs) : pointer(rhs.release()) {
    //
  }
  ~AutoPointer() {
    delete pointer;
    std::cout <<"free memory." <<std::endl;
  }

  template<typename U>
  AutoPointer<T>& operator=(AutoPointer<U> &rhs) {
    if (this != &rhs) {
      pointer = rhs.release();
    }
  }

  T* get() {
    return pointer;
  }

private:
  T *pointer;
};

int main() {
  AutoPointer<int> p(new int);
}

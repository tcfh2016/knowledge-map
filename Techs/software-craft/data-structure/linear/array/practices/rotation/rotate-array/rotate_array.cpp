#include <iostream>

void print(int arr[], int n) {
  for (auto i = 0; i < n; ++i) {
    std::cout <<arr[i] <<' ';
  }
  std::cout <<std::endl;
}

/* will reach time limit for big array.
void rotateArr1(int arr[], int d, int n) {
    while (d-- > 0) {
        auto tmp = arr[0];
        for (auto j = 1; j < n; ++j) {
            arr[j - 1] = arr[j];
        }
        arr[n - 1] = tmp;
    }
}
*/

void rotateArr2(int arr[], int d, int n) {
  int new_arr[d] = {};
  for (auto i = 0; i < d; ++i) {
    new_arr[i] = arr[i];
  }

  for (auto i = 0; i < n; ++i) {
    if (i + d > n - 1) {
      arr[i] = new_arr[(i + d) % n];
    }
    else {
      arr[i] = arr[i + d];
    }
  }
}

int main() {
  int arr[] = {1, 2, 3, 4, 5};
  rotateArr2(arr, 1, 5);
  print(arr, 5);

  return 0;
}

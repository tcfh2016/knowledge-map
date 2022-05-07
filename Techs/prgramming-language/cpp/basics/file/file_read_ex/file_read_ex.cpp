#include <iostream>
#include <fstream>
#include <string>

void printLastKLines(const char* filename, int k) {
  std::ifstream file(filename);
  std::string kStrings[k];

  int size = 0;
  while (file.good()) {
    std::getline(file, kStrings[size++%k]);
  }

  auto count = std::min(k, size);
  auto start = size > k ? size%k : 0;
  for (auto i = 0; i < count; ++i) {
    std::cout <<kStrings[(i+start) % k] <<std::endl;
  }
}

int main() {
  printLastKLines("test_data.txt", 3);
  return 0;
}

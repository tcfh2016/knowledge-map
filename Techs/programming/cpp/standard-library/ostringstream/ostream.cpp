#include <iostream>
#include <sstream>
#include <vector>
#include <cstdio>

int main() {
  std::vector<unsigned char> pucchList = {};
  std::ostringstream s;

  for(auto e : pucchList) {
    s <<static_cast<unsigned int>(e) <<",";
  }
  std::cout <<s.str() <<std::endl;
  printf("%s\n", s.str().c_str());
  return 0;
}

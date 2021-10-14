#include <iostream>
#include <bitset>
#include <cstring>

bool isUniqueChar_UsingBitset(const char *str) {
  const int MAX_ASCII_VALUE = 128;
  if (strlen(str) > MAX_ASCII_VALUE) {
    return false;
  }
  std::bitset<MAX_ASCII_VALUE> char_set;
  for (size_t i = 0; i < strlen(str); ++i) {
    if (char_set.test(str[i])) {
      return false;
    }
    char_set.set(str[i]);
  }
  return true;
}

bool isUniqueChar(const char *str) {
  const int MAX_ASCII_VALUE = 128;
  if (strlen(str) > MAX_ASCII_VALUE) {
    return false;
  }

  bool char_set[MAX_ASCII_VALUE] = {false};
  for (size_t i = 0; i < strlen(str); ++i) {
    size_t index = str[i];
    if (char_set[index]) {
      return false;
    }
    char_set[index] = true;
  }
  return true;
}

int main() {
  char test_chars1[] = "abd712a";
  char test_chars2[] = "abd712";
  //std::cout <<test_chars1 <<std::endl;
  //std::cout <<test_chars2 <<std::endl;
  std::cout <<test_chars1 <<" " <<isUniqueChar_UsingBitset(test_chars1) <<std::endl;
  std::cout <<test_chars2 <<" " <<isUniqueChar_UsingBitset(test_chars2) <<std::endl;
  std::cout <<test_chars1 <<" " <<isUniqueChar(test_chars1) <<std::endl;
  std::cout <<test_chars2 <<" " <<isUniqueChar(test_chars2) <<std::endl;

  return 0;
}

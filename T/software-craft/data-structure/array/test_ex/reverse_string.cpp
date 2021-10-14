#include <cstring>
#include <cstdio>
#include <iostream>

void reverse_c(char* str) {
  if (str == NULL) {
    return ;
  }

  for (int start = 0, end = strlen(str) - 1; start < end; ++start, --end) {
    char t = str[start];
    str[start] = str[end];
    str[end] = t;
  }
}

void reverse_cpp(char* str) {
  if (str == NULL) {
    return ;
  }
  // if can't use strlen(), must find the end char
  //char* end = str;
  //while (*end) {
  //  ++end;
  //}
  //--end;

  for (int start = 0, end = strlen(str) - 1; start < end; ++start, --end) {
    std::swap(str[start], str[end]);
  }
}

int main() {
  char test_str1[] = "nihao yoo";
  printf(test_str1);
  reverse_c(test_str1);
  printf(test_str1);

  reverse_cpp(test_str1);
  std::cout <<std::endl <<test_str1 <<std::endl;
  return 0;
}

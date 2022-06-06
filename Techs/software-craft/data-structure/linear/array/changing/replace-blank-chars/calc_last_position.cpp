#include <iostream>
#include <cstring>

void compress_string(char *str, int length)
{
  // find how many chars
  int charsCounter = 0;
  for (auto i = 0; i < length; ++i)
  {
    if (str[i] == ' ')
    {
      ++charsCounter;
    }
  }

  // calc the last position
  int last = charsCounter*2 + length;

  // copy from the end to beginning
  for (auto i = length; i >= 0; --i)
  {
    if (str[i] == ' ')
    {
      str[last--] = '0';
      str[last--] = '2';
      str[last--] = '%';
    }
    else
    {
      str[last--] = str[i];
    }
  }
}

int main()
{
  char test1[100] = "Mr John Smith";
  compress_string(test1, strlen(test1));
  std::cout <<test1 <<std::endl;
}

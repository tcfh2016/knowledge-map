#include <iostream>
#include <string>

std::string compress_string(const char *str, int length)
{
  std::cout <<"raw string content: " <<str <<std::endl;
  std::cout <<"raw string length : " <<length <<std::endl;
  std::string target;

  for (auto i = 0; i < length; ++i)
  {
    if (str[i] == ' ')
    {
      target += "%20";
    }
    else
    {
      target += str[i];
    }
  }

  return target;
}

int main()
{
  std::string test1{"Mr John Smith"};
  std::string ret = compress_string(test1.c_str(), test1.size());
  std::cout <<ret <<std::endl;
}

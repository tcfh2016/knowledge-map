#include <iostream>
#include <string>

std::string compress_string(std::string& source)
{
  std::string target;

  // compress
  char last = source[0];
  int cnt = 1;
  for (auto i = 1; i <= source.size(); ++i)
  {
    if (source[i] == last)
    {
      ++cnt;
    }
    else
    {
      target += last;
      target += ('0' + cnt);

      cnt = 1;
      last = source[i];
    }
  }

  if (target.size() >= source.size())
  {
    return source;
  }
  return target;
}

int main()
{
  std::string test1("aabcccccaaa");
  std::cout <<compress_string(test1) <<std::endl;
  return 0;
}

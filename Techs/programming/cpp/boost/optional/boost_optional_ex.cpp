#include <iostream>
#include <sstream>
#include <boost/optional.hpp>

boost::optional<int> convert(const std::string& text)
{
  boost::optional<int> result;
  std::stringstream s(text);
  int i;
  if ((s >> i) && s.get() == std::char_traits<char>::eof())
  {
    result = i;
  }

  return result;
}

int main()
{
  if (convert("100"))
  {
    std::cout <<convert("100").value() <<std::endl;
  }
  else
  {
    std::cout <<"hello world." <<std::endl;
  }

  return 0;
}

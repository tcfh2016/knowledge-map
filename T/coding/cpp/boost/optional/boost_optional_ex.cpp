#include <iostream>
#include <boost/optional.hpp>

boost::optional<int> convert(const std::string& text)
{
  std::stringstream s(text);
  int i;
  if ((s >> i) && s.get() == std::char_traits<char>::eof())
  {
    return i;
  }
  else
  {
    return boost::none;
  }
}

int main()
{
  return 0;
}

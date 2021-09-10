#include <iostream>
#include <vector>
#include <iterator>

int main()
{
  // c.reserve()
  std::vector<int> intVec;
  std::cout <<"intVec.capacity() = " <<intVec.capacity() <<std::endl;
  std::cout <<"intVec.max_size() = " <<intVec.max_size() <<std::endl;
  std::cout <<"intVec.size() = " <<intVec.size() <<std::endl;

  intVec.reserve(122);
  intVec.emplace_back(3);
  std::cout <<"intVec.capacity() = " <<intVec.capacity() <<std::endl;
  std::cout <<"intVec.max_size() = " <<intVec.max_size() <<std::endl;
  std::cout <<"intVec.size() = " <<intVec.size() <<std::endl;

  // c.capacity() with blank vector
  std::vector<int> intVec2;
  std::cout <<"intVec2.capacity() = " <<intVec2.capacity() <<std::endl;
  std::cout <<"intVec2.max_size() = " <<intVec2.max_size() <<std::endl;
  std::cout <<"intVec2.size() = " <<intVec2.size() <<std::endl;

  intVec2.emplace_back(3);
  std::cout <<"intVec2.capacity() = " <<intVec2.capacity() <<std::endl;
  std::cout <<"intVec2.max_size() = " <<intVec2.max_size() <<std::endl;
  std::cout <<"intVec2.size() = " <<intVec2.size() <<std::endl;

  // c.capacity() with non-blank vector: size != capacity
  std::vector<int> intVec3 = {1, 2, 3, 4, 5};
  std::cout <<"intVec3.capacity() = " <<intVec3.capacity() <<std::endl;
  std::cout <<"intVec3.max_size() = " <<intVec3.max_size() <<std::endl;
  std::cout <<"intVec3.size() = " <<intVec3.size() <<std::endl;

  intVec3.emplace_back(3); // capacity changes from 5 to 10 for this statement.
  std::cout <<"intVec3.capacity() = " <<intVec3.capacity() <<std::endl;
  std::cout <<"intVec3.max_size() = " <<intVec3.max_size() <<std::endl;
  std::cout <<"intVec3.size() = " <<intVec3.size() <<std::endl;

  std::copy(intVec3.begin(), intVec3.end(), std::ostream_iterator<int>(std::cout, " "));

}

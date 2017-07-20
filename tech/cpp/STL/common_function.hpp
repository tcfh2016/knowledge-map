#include <iostream>
#include <string>

template <typename T>
inline void PRINT_ELEMENTS(const T&col, const std::string& optstr="")
{
	std::cout <<optstr;
	for (typename T::const_iterator pos = col.begin(); pos != col.end(); ++pos)
	{
		std::cout <<*pos <<' ';
	}
	std::cout <<std::endl;
}

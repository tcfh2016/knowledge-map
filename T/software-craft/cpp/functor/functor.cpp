#include <iostream>
#include <vector>
#include <algorithm>

class PrintInt
{
	public:
		void operator()(int elem) const
		{
			std::cout <<elem <<' ';
		}
};

int main()
{
	std::vector<int> coll;

	for (int i=0; i<9; ++i)
	{
		coll.push_back(i);
	}

	for_each(coll.begin(), coll.end(), PrintInt());
	std::cout <<std::endl;
}

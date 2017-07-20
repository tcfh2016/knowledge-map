#include <iostream>
#include <list>
#include <algorithm>

int main()
{
	std::list<int> coll;

	for (int i=0; i < 6; ++i)
	{
		coll.push_front(i);
		coll.push_back(i);
	}

	coll.erase(remove(coll.begin(), coll.end(), 3), coll.end());

	coll.remove(4);

	return 0;
}

// ZipString.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
#include <map>

// Solution: read the string and count the repeated times for nearby chars.
std::string compressString(std::string &str)
{
	if (str.empty())
	{
		return str;
	}

	std::string ret;
	std::string::iterator start_index = str.begin();
	int count = 0;

	ret.push_back(*str.begin());
	for (std::string::iterator it = str.begin(); it != str.end(); ++it)
	{
		if (*it == *start_index)
		{
			count++;
		}
		else
		{
			ret.push_back('0' + count);
			
			ret.push_back(*it);
			start_index = it;
			count = 1;
		}
	}
	ret.push_back('0' + count);

	if (str.length() == ret.length())
	{
		return str;
	}
	else
	{
		return ret;
	}	
}

int main()
{
	std::string test("aabcccccaaa");

    std::cout << compressString(test) <<std::endl;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

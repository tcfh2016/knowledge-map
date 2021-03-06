// IfStringMatchAfterRotating.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <cstring>

bool MatchSameOrder(std::string targetStr, std::string sourceStr, int start)
{
	for (size_t i = 0; i < targetStr.length(); ++i)
	{
		if (targetStr[i] != sourceStr[(start + i)%sourceStr.length()])
		{
			return false;
		}
	}
	return true;	
}

bool IsStringMatchAfterRotating(std::string &str1, std::string &str2)
{
	if (str1.length() != str2.length())
	{
		return false;
	}

	int str1StartIndex = 0;
	for (size_t i = 0; i < str2.length(); ++i)
	{
		if ((str2[i] == str1[0]) && (MatchSameOrder(str1, str2, i)))
		{
			return true;			
		}
	}

	return false;
}

bool IsStringMatchAfterRotating_ByMoreEffeicientWay(std::string &str1, std::string &str2)
{
	if ((str1.length() == str2.length()) && (str1.length() != 0))
	{
		std::string temp = str1 + str1;
		return (NULL != temp.c_str(), str2.c_str());
	}
	return false;
}

int main()
{
	std::string testStr1("waterbottle");
	std::string testStr2("erbottlewat");
	

    std::cout << IsStringMatchAfterRotating(testStr1, testStr2) <<std::endl;
	std::cout << IsStringMatchAfterRotating_ByMoreEffeicientWay(testStr1, testStr2) << std::endl;

	return 0;	
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

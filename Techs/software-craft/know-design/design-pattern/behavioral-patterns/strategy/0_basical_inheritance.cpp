// 0_basical_inheritance.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

class Duck 
{
public:
	void quack()
	{
		std::cout << "Duck: quack()" << std::endl;
	}

	void swim()
	{
		std::cout << "Duck: swim()" << std::endl;
	}

	virtual void display()
	{
		std::cout << "Duck: display()" << std::endl;
	}
};

class MallardDuck : public Duck 
{
	virtual void display()
	{
		std::cout << "MallardDuck: display()" << std::endl;
	}
};

class RedheadDuck : public Duck 
{
	virtual void display()
	{
		std::cout << "RedheadDuck: display()" << std::endl;
	}
};

int main()
{
	Duck *mduck = new MallardDuck();
	mduck->quack();
	mduck->swim();
	mduck->display();

	Duck *rduck = new RedheadDuck();
	rduck->quack();
	rduck->swim();
	rduck->display();    
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

// DecoratorPattern.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>

class Beverage 
{
public:	
	virtual std::string getDescription() = 0;
	virtual double cost() = 0;
private:
	std::string description;
};

class HouseBlend : public Beverage 
{
public:
	HouseBlend() : description("HouseBlend") {}

	std::string getDescription()
	{
		return description;
	}
	double cost() 
	{
		return 1.0;
	}
private:
	std::string description;
};

class DarkRoast : public Beverage
{
public:
	DarkRoast() : description("DarkRoast") {}

	std::string getDescription()
	{
		return description;
	}
	double cost()
	{
		return 2.0;
	}
private:
	std::string description;
};

class Decaf : public Beverage
{
public:
	Decaf() : description("Decaf") {}

	std::string getDescription()
	{
		return description;
	}
	double cost()
	{
		return 3.0;
	}
private:
	std::string description;
};

class Espresso : public Beverage
{
public:
	Espresso() : description("Espresso") {}

	std::string getDescription()
	{
		return description;
	}
	double cost()
	{
		return 4.0;
	}
private:
	std::string description;
};

class Decorator : public Beverage
{
public:
	
	virtual std::string getDescription() = 0;	
	virtual double cost() = 0;
	
private:
	std::string description;
};

class Milk : public Decorator
{
public:
	Milk(Beverage &_beverage) : beverage(_beverage), description("Milk") {}

	std::string getDescription()
	{
		return beverage.getDescription() + ',' + description;
	}
	double cost()
	{
		return beverage.cost() + 0.1;
	}
private:
	Beverage &beverage;
	std::string description;
};

class Mocha : public Decorator
{
public:
	Mocha(Beverage &_beverage) : beverage(_beverage), description("Mocha") {}

	std::string getDescription()
	{
		return beverage.getDescription() + ',' + description;
	}
	double cost()
	{
		return beverage.cost() + 0.2;
	}
private:
	Beverage &beverage;
	std::string description;
};

class Soy : public Decorator
{
public:
	Soy(Beverage &_beverage) : beverage(_beverage), description("Soy") {}

	std::string getDescription()
	{
		return beverage.getDescription() + ',' + description;
	}
	double cost()
	{
		return beverage.cost() + 0.3;
	}
private:
	Beverage &beverage;
	std::string description;
};

class Whip : public Decorator
{
public:
	Whip(Beverage &_beverage) : beverage(_beverage), description("Whip") {}

	std::string getDescription()
	{
		return beverage.getDescription() + ',' + description;
	}
	double cost()
	{
		return beverage.cost() + 0.4;
	}
private:
	Beverage &beverage;
	std::string description;
};

int main()
{
	Beverage *beverage = new Espresso();
	beverage = new Whip(*beverage);
	beverage = new Milk(*beverage);

	std::string des = beverage->getDescription() + " $";

    std::cout<< des << beverage->cost() <<std::endl;
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

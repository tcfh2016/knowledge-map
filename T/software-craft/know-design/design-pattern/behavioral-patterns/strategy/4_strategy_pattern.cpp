// 4_strategy_pattern.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

class FlyBehavior
{
public:
	virtual void fly() = 0;
};

class FlayWithWings : public FlyBehavior
{
public:
	virtual void fly()
	{
		std::cout << "Fly with wings!" << std::endl;
	}
};

class FlayWithNoWing : public FlyBehavior
{
public:
	virtual void fly()
	{
		std::cout << "Fly with no wing!" << std::endl;
	}
};

class Duck
{
public:
	Duck() : flyBehavior(NULL){}

	void quack()
	{
		std::cout << "quack()" << std::endl;
	}

	void swim()
	{
		std::cout << "swim()" << std::endl;
	}

	void fly()
	{
		flyBehavior->fly();
	}

	void setFlyBehavior(FlyBehavior *b)
	{
		flyBehavior = b;
	}

	virtual void display()
	{
		std::cout << "display()" << std::endl;
	}

	FlyBehavior *flyBehavior;
};

class MallardDuck : public Duck
{
public:
	MallardDuck()
	{
		flyBehavior = new FlayWithWings();
	}

	virtual void display()
	{
		std::cout << "MallardDuck: display()" << std::endl;
	}	
};

class RedheadDuck : public Duck
{
public:
	RedheadDuck()
	{
		flyBehavior = new FlayWithWings();
	}

	virtual void display()
	{
		std::cout << "RedheadDuck: display()" << std::endl;
	}	
};

class RubberDuck : public Duck
{
public:
	RubberDuck()
	{
		flyBehavior = new FlayWithNoWing();
	}

	virtual void display()
	{
		std::cout << "RubberDuck: display()" << std::endl;
	}	
};

class DecoyDuck : public Duck
{
public:
	DecoyDuck()
	{
		flyBehavior = new FlayWithNoWing();
	}

	virtual void display()
	{
		std::cout << "DecoyDuck: display()" << std::endl;
	}	
};

int main()
{
	MallardDuck *mallarDuck = new MallardDuck();
	mallarDuck->quack();
	mallarDuck->swim();
	mallarDuck->fly();
	mallarDuck->display();

	RedheadDuck *redheadDuck = new RedheadDuck();
	redheadDuck->quack();
	redheadDuck->swim();
	redheadDuck->fly();
	redheadDuck->display();

	RubberDuck *rubberDuck = new RubberDuck();
	rubberDuck->quack();
	rubberDuck->swim();
	rubberDuck->fly();
	rubberDuck->display();

	DecoyDuck *decoyDuck = new DecoyDuck();
	decoyDuck->quack();
	decoyDuck->swim();
	decoyDuck->fly();
	decoyDuck->display();

	FlayWithWings *newFlyBehavior = new FlayWithWings();
	decoyDuck->setFlyBehavior(newFlyBehavior);
	decoyDuck->fly();
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

#include <iostream>

class CaffeineBeverage 
{
public:
	virtual void prepareRecipe()
	{
		boilWater();
		brew();
		pourInCup();
		addCondiments();
	}

	virtual void brew() = 0;
	virtual void addCondiments() = 0;

	void boilWater()
	{
		std::cout <<"Boiling water" <<std::endl;
	}

	void pourInCup()
	{
		std::cout <<"Pouring into cup" <<std::endl;
	}
};
	
class Coffee : public CaffeineBeverage
{
public:

	void brew()
	{
		std::cout <<"Dripping Coffee through filter" <<std::endl;
	}

	void addCondiments()
	{
		std::cout <<"Adding Sugar and Milk" <<std::endl;
	}
};

class Tea : public CaffeineBeverage
{
public:

	void brew()
	{
		std::cout <<"Steeping the tea" <<std::endl;
	}

	void addCondiments()
	{
		std::cout <<"Adding Lemon" <<std::endl;
	}
};


int main()
{
	Coffee coffee;
	coffee.prepareRecipe();

	Tea tea;
	tea.prepareRecipe();
}

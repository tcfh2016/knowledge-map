#include <iostream>

class CaffeineBeverage 
{
public:
	virtual void prepareRecipe()
	{
	}

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

	void prepareRecipe()
	{
		boilWater();
		brewCoffeeGrinds();
		pourInCup();
		addSugarAndMilk();
	}

	void brewCoffeeGrinds()
	{
		std::cout <<"Dripping Coffee through filter" <<std::endl;
	}

	void addSugarAndMilk()
	{
		std::cout <<"Adding Sugar and Milk" <<std::endl;
	}
};

class Tea : public CaffeineBeverage
{
public:

	void prepareRecipe()
	{
		boilWater();
		steepTeaBag();
		pourInCup();
		addLemon();
	}

	void steepTeaBag()
	{
		std::cout <<"Steeping the tea" <<std::endl;
	}

	void addLemon()
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

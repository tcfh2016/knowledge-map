#include <iostream>

class Coffee
{
public:

	void prepareRecipe()
	{
		boilWater();
		brewCoffeeGrinds();
		pourInCup();
		addSugarAndMilk();
	}

	void boilWater()
	{
		std::cout <<"Boiling water" <<std::endl;
	}

	void brewCoffeeGrinds()
	{
		std::cout <<"Dripping Coffee through filter" <<std::endl;
	}
	void pourInCup()
	{
		std::cout <<"Pouring into cup" <<std::endl;
	}
	void addSugarAndMilk()
	{
		std::cout <<"Adding Sugar and Milk" <<std::endl;
	}
};

class Tea 
{
public:

	void prepareRecipe()
	{
		boilWater();
		steepTeaBag();
		pourInCup();
		addLemon();
	}

	void boilWater()
	{
		std::cout <<"Boiling water" <<std::endl;
	}

	void steepTeaBag()
	{
		std::cout <<"Steeping the tea" <<std::endl;
	}
	void pourInCup()
	{
		std::cout <<"Pouring into cup" <<std::endl;
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

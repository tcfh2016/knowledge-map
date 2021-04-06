#include <iostream>

class Drink
{
public:
	virtual void prepareRecipe()
	{
		boilWater();
		steep();
		pourInCup();
		addFlavour();
	}

	void boilWater()
	{
		std::cout <<"Boiling water" <<std::endl;
	}

	virtual void steep()
	{
		std::cout <<"Steeping..." <<std::endl;
	}

	void pourInCup()
	{
		std::cout <<"Pouring into cup" <<std::endl;
	}
	
	virtual void addFlavour()
	{
		std::cout <<"Adding Flavour..." <<std::endl;
	}
};
	
class Coffee : public Drink
{
public:

	void prepareRecipe()
	{
		boilWater();
		steep();
		pourInCup();
		addFlavour();
	}

	void steep()
	{
		std::cout <<"Dripping Coffee through filter" <<std::endl;
	}
	void addFlavour()
	{
		std::cout <<"Adding Sugar and Milk" <<std::endl;
	}
};

class Tea : public Drink
{
public:

	void prepareRecipe()
	{
		boilWater();
		steep();
		pourInCup();
		addFlavour();
	}

	void steep()
	{
		std::cout <<"Steeping the tea" <<std::endl;
	}

	void addFlavour()
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

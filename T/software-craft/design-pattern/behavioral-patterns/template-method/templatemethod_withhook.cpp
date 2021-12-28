#include <iostream>

class CaffeineBeverage 
{
public:
	virtual void prepareRecipe()
	{
		boilWater();
		brew();
		pourInCup();
		if (customerWantsCondiments())
		{
			addCondiments();
		}
	}

	virtual void brew() = 0;
	virtual void addCondiments() = 0;
	virtual bool customerWantsCondiments()
	{
		return true;
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
	
class CoffeeWithHook : public CaffeineBeverage
{
public:
	std::string getUserChoice()
	{
		std::string input;
		std::cout <<"Wanna some condiments ?" <<std::endl;
		std::cin >>input;

		return input;
	}
		
	bool customerWantsCondiments()
	{
		std::string answer = getUserChoice();
		if (std::string::npos != answer.find('y'))
		{
			return true;
		}
		else
		{
			return false;
		}
	}

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
	CoffeeWithHook coffee;
	coffee.prepareRecipe();

	Tea tea;
	tea.prepareRecipe();
}

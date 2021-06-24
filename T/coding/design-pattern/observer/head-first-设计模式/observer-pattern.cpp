// observer-pattern.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <vector>
#include <list>

class Observer
{
public:
	virtual void update(double temperature, double humidity, double pressure) = 0;
};

class Subject
{
public:
	virtual void registerObserver(Observer *observer) = 0;
	virtual void removeObserver(Observer *observer) = 0;
	virtual void notifyObserver(double temperature, double humidity, double pressure) = 0;
};

class WeatherData : public Subject
{
public:
	double getTemperature()
	{
		return 23.00;
	}

	double getHumidity()
	{
		return 60.00;
	}

	double getPressure()
	{
		return 1022.00;
	}

	virtual void registerObserver(Observer *observer)
	{
		observerList.push_back(observer);
	}

	virtual void removeObserver(Observer *observer)
	{
		observerList.remove(observer);
	}

	virtual void notifyObserver(double temperature, double humidity, double pressure)
	{
		//for_each();
		for (std::list<Observer *>::iterator iter = observerList.begin(); iter != observerList.end(); ++iter)
		{
			(*iter)->update(temperature, humidity, pressure);
		}
	}

	void measurementChange()
	{
		double temperature = getTemperature();
		double humidity = getHumidity();
		double pressure = getPressure();

		notifyObserver(temperature, humidity, pressure);
	}

private:
	std::list<Observer *> observerList;
};


class ConditionDisplay : public Observer
{
public:
	ConditionDisplay(Subject &subject)
	{
		subject.registerObserver(this);
	}

	void update(double temperature, double humidity, double pressure)
	{
		std::cout << "Contion Display: \n" \
			<< "\t temperature: " << temperature \
			<< "\t humidity: " << humidity \
			<< "\t pressure: " << pressure << std::endl;
	}
};

class StatisticsDisplay : public Observer
{
public:
	StatisticsDisplay(Subject &subject)
	{
		subject.registerObserver(this);
	}

	void update(double temperature, double humidity, double pressure)
	{
		std::cout << "Statistics Display: \n" \
			<< "\t temperature: " << temperature \
			<< "\t humidity: " << humidity \
			<< "\t pressure: " << pressure << std::endl;
	}
};

class ForecastDisplay : public Observer
{
public:
	ForecastDisplay(Subject &subject)
	{
		subject.registerObserver(this);
	}

	void update(double temperature, double humidity, double pressure)
	{
		std::cout << "Forecast Display: \n" \
			<< "\t temperature: " << temperature \
			<< "\t humidity: " << humidity \
			<< "\t pressure: " << pressure <<std::endl;
	}
};


int main()
{
	WeatherData wetherData;

	ConditionDisplay conditionDisplay(wetherData);
	StatisticsDisplay statisticsDisplay(wetherData);
	ForecastDisplay forcastDisplay(wetherData);

	wetherData.measurementChange();
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

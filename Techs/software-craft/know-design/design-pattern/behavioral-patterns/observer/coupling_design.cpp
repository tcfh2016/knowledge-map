// observer-pattern.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

class ConditionDisplay
{
public:
	void update(double temperature, double humidity, double pressure)
	{
		std::cout << "Contion Display: \n" \
			<< "\t temperature: " << temperature \
			<< "\t humidity: " << humidity \
			<< "\t pressure: " << pressure << std::endl;
	}
};

class StatisticsDisplay
{
public:
	void update(double temperature, double humidity, double pressure)
	{
		std::cout << "Statistics Display: \n" \
			<< "\t temperature: " << temperature \
			<< "\t humidity: " << humidity \
			<< "\t pressure: " << pressure << std::endl;
	}
};

class ForecastDisplay
{
public:
	void update(double temperature, double humidity, double pressure)
	{
		std::cout << "Forecast Display: \n" \
			<< "\t temperature: " << temperature \
			<< "\t humidity: " << humidity \
			<< "\t pressure: " << pressure <<std::endl;
	}
};

class WeatherData
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

	void measurementChange()
	{
		double temperature = getTemperature();
		double humidity = getHumidity();
		double pressure = getPressure();

		conditionDisplay.update(temperature, humidity, pressure);
		statisticsDisplay.update(temperature, humidity, pressure);
		forecastDisplay.update(temperature, humidity, pressure);
	}

private:
	ConditionDisplay conditionDisplay;
	StatisticsDisplay statisticsDisplay;
	ForecastDisplay forecastDisplay;
};

int main()
{
	WeatherData wetherData;

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

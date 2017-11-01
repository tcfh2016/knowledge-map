#ifndef _STOCKOBSERVER_HPP_
#define _STOCKOBSERVER_HPP_

#include "observer.hpp"
#include "secretary.hpp"
#include <iostream>

class StockObserver : public Observer
{
public:
  StockObserver(std::string name, Secretary *secretary) : Observer(name, secretary)
  {
  }
  ~StockObserver(){}

  void update()
  {
    std::cout <<Observer::_secretary->getAction() <<Observer::_name <<" close stock windows, keep on working." <<std::endl;
  }
};

#endif

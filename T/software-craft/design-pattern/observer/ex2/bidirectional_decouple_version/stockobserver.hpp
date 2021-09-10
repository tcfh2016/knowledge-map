#ifndef _STOCKOBSERVER_HPP_
#define _STOCKOBSERVER_HPP_

#include "observer.hpp"
#include "subject.hpp"
#include <iostream>

class StockObserver : public Observer
{
public:
  StockObserver(std::string name, Subject *subject) : Observer(name, subject)
  {
  }
  ~StockObserver(){}

  void update()
  {
    std::cout <<Observer::_subject->getAction() <<Observer::_name <<" close stock windows, keep on working." <<std::endl;
  }
};

#endif

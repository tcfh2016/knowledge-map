#ifndef _SECRETARY_HPP_
#define _SECRETARY_HPP_

#include <string>
#include <list>
#include "stockobserver.hpp"
#include <iostream>

class Secretary
{
public:
  Secretary(){}
  ~Secretary(){}

  void attach(StockObserver observer);
  void notify();

  void setAction(std::string action)
  {
    _action = action;    
  }

  std::string getAction()
  {
    return _action;
  }

private:
  std::string _action;
  std::list<StockObserver> _observers;
};

#endif

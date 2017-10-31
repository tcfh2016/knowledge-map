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

  std::string setAction(std::string action)
  {
    _action = action;

    std::cout <<"setAction: " <<_action <<std::endl;
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

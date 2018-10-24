#ifndef _SECRETARY_HPP_
#define _SECRETARY_HPP_

#include <string>
#include <list>
#include "observer.hpp"
#include <iostream>

class Secretary
{
public:
  Secretary(){}
  ~Secretary(){}

  void attach(Observer *observer);
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
  std::list<Observer *> _observers;
};

#endif

#ifndef _SUBJECT_HPP_
#define _SUBJECT_HPP_

#include <string>
#include <list>
#include "observer.hpp"
#include <iostream>

class Subject
{
public:
  Subject(){}
  ~Subject(){}

  void attach(Observer *observer);
  void dettach(Observer *observer);
  void notify();

  void setAction(std::string action)
  {
    _action = action;
  }

  std::string getAction()
  {
    return _action;
  }

protected:
  std::string _action;
  std::list<Observer *> _observers;
};

#endif

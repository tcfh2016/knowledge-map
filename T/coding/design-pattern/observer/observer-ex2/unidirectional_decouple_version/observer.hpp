#ifndef _OBSERVER_HPP_
#define _OBSERVER_HPP_

#include <string>

class Secretary;

class Observer
{
public:
  Observer(std::string name, Secretary *secretary)
  {
    _name = name;
    _secretary = secretary;
  }
  ~Observer(){}

  virtual void update() = 0;

protected:
  std::string _name;
  Secretary *_secretary;
};

#endif

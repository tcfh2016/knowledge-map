#ifndef _NBAOBSERVER_HPP_
#define _NBAOBSERVER_HPP_

#include "observer.hpp"
#include "secretary.hpp"
#include <iostream>

class NbaObserver : public Observer
{
public:
  NbaObserver(std::string name, Secretary *secretary) : Observer(name, secretary)
  {
  }
  ~NbaObserver(){}

  void update()
  {
    std::cout <<Observer::_secretary->getAction() <<Observer::_name <<" close vedio window, keep on working." <<std::endl;
  }
};

#endif

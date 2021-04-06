#ifndef _NBAOBSERVER_HPP_
#define _NBAOBSERVER_HPP_

#include "observer.hpp"
#include "subject.hpp"
#include <iostream>

class NbaObserver : public Observer
{
public:
  NbaObserver(std::string name, Subject *subject) : Observer(name, subject)
  {
  }
  ~NbaObserver(){}

  void update()
  {
    std::cout <<Observer::_subject->getAction() <<Observer::_name <<" close vedio window, keep on working." <<std::endl;
  }
};

#endif

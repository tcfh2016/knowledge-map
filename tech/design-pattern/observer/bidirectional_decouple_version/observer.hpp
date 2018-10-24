#ifndef _OBSERVER_HPP_
#define _OBSERVER_HPP_

#include <string>

class Subject;

class Observer
{
public:
  Observer(std::string name, Subject *subject)
  {
    _name = name;
    _subject = subject;
  }
  ~Observer(){}

  virtual void update() = 0;

protected:
  std::string _name;
  Subject *_subject;
};

#endif

#include "secretary.hpp"

void Secretary::attach(Observer* observer)
{
  _observers.push_back(observer);
}

void Secretary::notify()
{
  std::cout <<"start notifying, stock observer number = " <<_observers.size() <<std::endl;

  for (std::list<Observer *>::iterator iter = _observers.begin();
    iter != _observers.end();
    ++iter)
  {
    (*iter)->update();
  }
}

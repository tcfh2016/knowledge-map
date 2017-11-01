#include "subject.hpp"

void Subject::attach(Observer* observer)
{
  _observers.push_back(observer);
}

void Subject::dettach(Observer* observer)
{
  _observers.remove(observer);
}

void Subject::notify()
{
  std::cout <<"start notifying, stock observer number = " <<_observers.size() <<std::endl;

  for (std::list<Observer *>::iterator iter = _observers.begin();
    iter != _observers.end();
    ++iter)
  {
    (*iter)->update();
  }
}

#include <iostream>
#include <list>

//class StockObserver;
class Secretary;

class StockObserver
{
public:
  StockObserver(std::string name, Secretary secretary)
  {
    _name = name;
    _secretary = secretary;
  }
  ~StockObserver(){}

  void update()
  {
    std::cout <<_secretary.getAction() <<_name <<" close stock windows, keep on working." <<std::endl;
  }

private:
  std::string _name;
  Secretary _secretary;
};

class Secretary
{
public:
  Secretary(){}
  ~Secretary(){}

  void attach(StockObserver observer)
  {
    _observers.push_back(observer);
  }

  void notify()
  {
    for (std::list<StockObserver>::iterator iter = _observers.begin();
      iter != _observers.end();
      ++iter)
    {
      iter->update();
    }
  }

  std::string setAction(std::string action)
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


int main()
{
  Secretary *s = new Secretary();
  StockObserver *t1 = new StockObserver("App", *s);
  StockObserver *t2 = new StockObserver("Bpp", *s);

  s->setAction("Boss is coming.");
  s->notify();

  return 0;
}

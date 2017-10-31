#ifndef _STOCKOBSERVER_HPP_
#define _STOCKOBSERVER_HPP_

#include <string>

class Secretary;

class StockObserver
{
public:
  StockObserver(std::string name, Secretary *secretary)
  {
    _name = name;
    _secretary = secretary;    
  }
  ~StockObserver(){}

  void update();

private:
  std::string _name;
  Secretary *_secretary;
};

#endif

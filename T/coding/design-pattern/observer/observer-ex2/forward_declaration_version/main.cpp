#include <iostream>
#include "stockobserver.hpp"
#include "secretary.hpp"

int main()
{
  std::cout <<"start" <<std::endl;

  Secretary *s = new Secretary();
  std::cout <<"one secretary was created." <<std::endl;

  StockObserver *t1 = new StockObserver("App", s);
  StockObserver *t2 = new StockObserver("Bpp", s);
  std::cout <<"two stock observer were created." <<std::endl;

  s->attach(*t1);
  s->attach(*t2);
  std::cout <<"two stock observer were attached." <<std::endl;

  s->setAction("Boss is coming.");
  s->notify();

  return 0;
}

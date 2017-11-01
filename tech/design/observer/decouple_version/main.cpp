#include <iostream>
#include "stockobserver.hpp"
#include "nbaobserver.hpp"
#include "secretary.hpp"

int main()
{
  std::cout <<"start" <<std::endl;

  Secretary *s = new Secretary();
  std::cout <<"one secretary was created." <<std::endl;

  Observer *t1 = new StockObserver("App", s);
  Observer *t2 = new NbaObserver("Bpp", s);
  std::cout <<"two stock observer were created." <<std::endl;

  s->attach(t1);
  s->attach(t2);
  std::cout <<"two stock observer were attached." <<std::endl;

  s->setAction("Boss is coming.");
  s->notify();

  return 0;
}

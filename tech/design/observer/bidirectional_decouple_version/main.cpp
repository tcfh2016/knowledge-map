#include <iostream>
#include "stockobserver.hpp"
#include "nbaobserver.hpp"
#include "secretary.hpp"
#include "boss.hpp"

int main()
{
  std::cout <<"start" <<std::endl;

  Subject *s = new Secretary();
  std::cout <<"one secretary was created." <<std::endl;
  Subject *b = new Boss();
  std::cout <<"one boss was created." <<std::endl;

  Observer *t1 = new StockObserver("App", s);
  s->attach(t1);
  std::cout <<"one stock observer was created and attached into secretary's list." <<std::endl;

  Observer *t2 = new NbaObserver("Bpp", b);
  b->attach(t2);
  std::cout <<"one NBA observer was created and attached into boss's list." <<std::endl;

  s->setAction("Boss is coming.");
  s->notify();

  b->setAction("Boss step in...");
  b->notify();

  return 0;
}

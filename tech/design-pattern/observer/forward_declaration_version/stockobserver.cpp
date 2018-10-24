#include "stockobserver.hpp"
#include "secretary.hpp"

#include <iostream>

void StockObserver::update()
{
  std::cout <<_secretary->getAction() <<_name <<" close stock windows, keep on working." <<std::endl;
}

#include "turkey_adapter.hpp"

int main()
{
  Duck *duck = new MallardDuck();
  duck->quack();
  duck->fly();

  Turkey *turkey = new WildTurkey();
  turkey->gobble();
  turkey->fly();


  Duck *turkeyAdapter = new TurkeyAdapter(turkey);
  turkeyAdapter->quack();
  turkeyAdapter->fly();

  return 0;
}

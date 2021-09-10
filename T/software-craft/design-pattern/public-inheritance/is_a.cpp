#include <iostream>

class FlyBehavior
{
public:
  virtual void fly() = 0;
};

class FlyWithWings : public FlyBehavior
{
public:
  FlyWithWings(){}
  ~FlyWithWings(){}

  void fly ()
  {
    std::cout <<"Flying with wings." <<std::endl;
  }
};

class FlyNoWay : public FlyBehavior
{
public:
  FlyNoWay(){}
  ~FlyNoWay(){}

  void fly () 
  {
    std::cout <<"No way to fly. DEBUG INFO..." <<std::endl;
  }
};

class Bird
{
public:
  ~Bird(){}
  Bird():flyBehavior(NULL)
  {
  }

  void fly()
  {
    flyBehavior->fly();
  }

  FlyBehavior *flyBehavior;
};

class Penguin : public Bird
{
public:
  ~Penguin(){}

  Penguin()
  {
    flyBehavior = new FlyNoWay();
  }
};

class Magpie : public Bird
{
public:
  ~Magpie(){}

  Magpie()
  {
    flyBehavior = new FlyWithWings();
  }
};

int main()
{
  Bird *m = new Magpie();
  m->fly();

  Bird *p = new Penguin();
  p->fly();

  return 0;
}

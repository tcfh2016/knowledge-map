#include <iostream>
#include <cmath>

class Operation
{
public:
  Operation(){}
  ~Operation(){}

  virtual double calculate() { return 0.0; }
  double getNumberA() { return numberA; }
  double getNumberB() { return numberB; }

  double setNumberA(double f) { numberA = f; }
  double setNumberB(double f) { numberB = f; }

protected:
  double numberA;
  double numberB;
};

class Add : public Operation
{
public:
  double calculate()
  {
    return (numberA + numberB);
  }
};

class Sub : public Operation
{
public:
  double calculate()
  {
    return (numberA - numberB);
  }
};

class Mul : public Operation
{
public:
  double calculate()
  {
    return (numberA * numberB);
  }
};

class Div : public Operation
{
public:
  double calculate()
  {
    static const double EPSINON = 0.00001f;
    if (fabs(numberB) < 1e6)
    {
      std::cout <<"The divisor can't be zero." <<std::endl;
      return 0.0;
    }
    else
    {
      return (numberA / numberB);
    }
  }
};

class OperationFactory
{
public:

  static Operation* getOperation(char opera)
  {
    Operation *opertion = NULL;

    switch (opera)
    {
      case '+':
      {
        opertion = new Add();
        break;
      }
      case '-':
      {
        opertion = new Sub();
        break;
      }
      case '*':
      {
        opertion = new Mul();
        break;
      }
      case '/':
      {
        opertion = new Div();
        break;
      }
      default:
      {
        std::cout <<"Invalid operator:" <<opera <<std::endl;
        break;
      }
    }

    return opertion;
  }
};


int main()
{
  double numberA = 0.0;
  double numberB = 0.0;
  char   opera   = '+';

  std::cout <<"Input number A: " <<std::endl;
  std::cin >>numberA;
  std::cout <<"Input operator: (only support +-*/)" <<std::endl;
  std::cin >>opera;
  std::cout <<"Input number B: " <<std::endl;
  std::cin >>numberB;

  Operation *op = OperationFactory::getOperation(opera);
  op->setNumberA(numberA);
  op->setNumberB(numberB);
  std::cout <<numberA <<opera <<numberB <<" = " <<op->calculate() <<std::endl;

  return 0;
}

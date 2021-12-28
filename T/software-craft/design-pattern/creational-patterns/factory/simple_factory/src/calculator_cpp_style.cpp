#include <iostream>
#include <cmath>

class Operation
{
public:

  static double calculate(double numberA, char opera, double numberB)
  {
    double result = 0.0;

    switch (opera)
    {
      case '+':
      {
        result = numberA + numberB;
        break;
      }
      case '-':
      {
        result = numberA - numberB;
        break;
      }
      case '*':
      {
        result = numberA * numberB;
        break;
      }
      case '/':
      {
        static const double EPSINON = 0.00001f;
        if (fabs(numberB) < 1e6)
        {
          std::cout <<"The divisor can't be zero." <<std::endl;
        }
        else
        {
          result = numberA / numberB;
        }
        break;
      }
      default:
      {
        std::cout <<"Invalid operator:" <<opera <<std::endl;
        break;
      }
    }
    return result;
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

  double result = Operation::calculate(numberA, opera, numberB);
  std::cout <<numberA <<opera <<numberB <<" = " <<result <<std::endl;

  return 0;
}

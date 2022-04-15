import decimal
from decimal import Decimal

decimal.getcontext().prec = 4

print(Decimal(1)/3)

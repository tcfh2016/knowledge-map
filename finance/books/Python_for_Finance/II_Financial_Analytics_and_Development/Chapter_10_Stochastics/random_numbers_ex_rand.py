import numpy as np
import numpy.random as npr

print(npr.rand(10))
print(npr.rand(5,5))

a = 5.
b = 10.
print(npr.rand(10) * (b - a) + a)

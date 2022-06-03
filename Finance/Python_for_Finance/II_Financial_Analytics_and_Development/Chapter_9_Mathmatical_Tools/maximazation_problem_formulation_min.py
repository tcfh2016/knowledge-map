import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.interpolate as spi
import scipy.optimize as spo

# function to be minimized
from math import sqrt
def Eu(s, b):    
    return -(0.5 * sqrt(s * 15 + b * 5) + 0.5 * sqrt(s * 5 + b * 12))
# constraints
cons = ({'type':'ineq', 'fun':(lambda s,b:100-s*10-b*10)})
# budget constraint
bnds = ((0, 1000), (0, 1000))  # uppper bounds large enough

result = spo.minimize(Eu, [5, 5], method='SLSQP', bounds=bnds, constraints=cons)
print(result)

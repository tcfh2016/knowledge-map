import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def f(x):
    return np.sin(x) + 0.5 * x

a = 0.5
b = 9.5

print(sci.fixed_quad(f, a, b))
print(sci.quad(f, a, b))
print(sci.romberg(f, a, b))

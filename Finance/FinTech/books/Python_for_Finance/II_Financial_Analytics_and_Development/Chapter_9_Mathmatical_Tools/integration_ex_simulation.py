import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def f(x):
    return np.sin(x) + 0.5 * x

a = 0.5
b = 9.5

for i in range(1, 20):
    np.random.seed(1000)
    x = np.random.random(i * 10) * (b - a) + a
    print(np.sum(f(x)) / len(x) * (b - a))

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5*x

x = np.linspace(-2*np.pi, 2*np.pi, 50)

#plt.rc('grid', linestyle="--", color='black')
plt.plot(x, f(x), 'b')
plt.grid(True)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

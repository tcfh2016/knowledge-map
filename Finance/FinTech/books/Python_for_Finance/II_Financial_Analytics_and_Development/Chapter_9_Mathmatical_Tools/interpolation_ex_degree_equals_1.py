import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spi

x = np.linspace(-2*np.pi, 2*np.pi, 25)

def f(x):
    return np.sin(x) + 0.5*x

ipo = spi.splrep(x, f(x), k=1)
iy = spi.splev(x, ipo)
print(np.allclose(f(x), iy))

plt.plot(x, f(x), 'b', label='f(x)')
plt.plot(x, iy, 'r.', label='interpolation')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

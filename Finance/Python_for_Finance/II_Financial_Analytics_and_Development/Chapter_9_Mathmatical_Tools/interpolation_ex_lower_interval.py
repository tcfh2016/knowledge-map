import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spi

x = np.linspace(-2*np.pi, 2*np.pi, 25)
xd = np.linspace(1.0, 3.0, 50)

def f(x):
    return np.sin(x) + 0.5*x

ipo = spi.splrep(x, f(x), k=1)
iy = spi.splev(x, ipo)
iyd = spi.splev(xd, ipo)
print(np.allclose(f(x), iy))

plt.plot(xd, f(xd), 'b', label='f(x)')
plt.plot(xd, iyd, 'r.', label='interpolation')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

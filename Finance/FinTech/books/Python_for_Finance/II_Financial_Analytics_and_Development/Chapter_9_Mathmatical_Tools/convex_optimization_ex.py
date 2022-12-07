import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.interpolate as spi
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)

def fm(x, y):
    return (np.sin(x) + 0.05*x**2 + np.sin(y) + 0.05*y**2)

X, Y = np.meshgrid(x, y)
Z = fm(X, Y)

fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
                       cmap=mpl.cm.coolwarm,
                       linewidth=0.5, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

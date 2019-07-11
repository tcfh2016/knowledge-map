import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


# 更改原始函数为高阶函数

def fm(x, y):
    return np.sin(x) + 0.25*x + np.sqrt(y) + 0.05 * y ** 2

# 由于此时fm是二元多项式，因此在构造数据时需要构造二阶数据
x = np.linspace(0, 10, 20)
print(x)
y = np.linspace(0, 10, 20)
print(y)
X, Y = np.meshgrid(x, y)
print(X)

Z = fm(X, Y)
x = X.flatten()
y = Y.flatten()

fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
                       cmap = mpl.cm.coolwarm,
                       linewidth=0.5, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

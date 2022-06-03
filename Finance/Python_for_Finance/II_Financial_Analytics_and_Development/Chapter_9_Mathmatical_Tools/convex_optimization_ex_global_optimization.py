import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy.interpolate as spi
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as spo

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)

def fo(x, *params):
    x,y = x
    z = np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2
    if output == True:
        print ('%8.4f %8.4f %8.4f' %(x, y, z))
    return z

def fm(x, *params):
    x,y = x
    return (np.sin(x) + 0.05*x**2 + np.sin(y) + 0.05*y**2)

# 选择步长为5进行搜索
output = True
spo.brute(fo, ((-10, 10.1, 5), (-10, 10.1, 5)), finish=None)

# 选择步长为0.1进行搜索
output = False
opt1 = spo.brute(fo, ((-10, 10.1, 0.1), (-10, 10.1, 0.1)), finish=None)
print(opt1)

# 根据坐标打印出Z轴的值
print(fm(opt1))

'''
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
'''

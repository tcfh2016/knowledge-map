import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.api as sm

# 更改原始函数为高元函数
def fm(x, y):
    return np.sin(x) + 0.25*x + np.sqrt(y) + 0.05 * y ** 2

# 创建二维的坐标系，并求取二维坐标系对应的函数值
x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y)
Z = fm(X, Y)
x = X.flatten()
y = Y.flatten()

# 基于x坐标值创建不同幂次的数组
# 由于我们已知了原始函数，因此我们能够给出恰好的估值函数
matrix = np.zeros((len(x), 6 + 1))

matrix[:, 6] = np.sqrt(y)
matrix[:, 5] = np.sin(x)
matrix[:, 4] = y ** 2
matrix[:, 3] = x ** 2
matrix[:, 2] = y
matrix[:, 1] = x
matrix[:, 0] = 1

# 回归函数
def reg_func(a, x, y):
    f6 = a[6] * np.sqrt(y)
    f5 = a[5] * np.sin(x)
    f4 = a[4] * y ** 2
    f3 = a[3] * x ** 2
    f2 = a[2] * y
    f1 = a[1] * x
    f0 = a[0] * 1
    return (f6 + f5 + f4 + f3 + f2 + f1 + f0)

model = sm.OLS(fm(x, y), matrix).fit()
a = model.params
RZ = reg_func(a, X, Y)

fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')
#surf1 = ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
#                       cmap = mpl.cm.coolwarm,
#                       linewidth=0.5, antialiased=True)
surf2 = ax.plot_surface(X, Y, RZ, rstride=2, cstride=2,
                       label='regression')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
#ax.legend()
#fig.colorbar(surf1, shrink=0.5, aspect=5)

plt.show()

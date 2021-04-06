import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5*x

x = np.linspace(-2*np.pi, 2*np.pi, 50)

# 获取函数 f(x) 的最优系数，这个系数对整个函数通用。
# 1. 指定 degree = 1，多项式只有2项，对应系数为2，因此图形的拟合度不好。
# 2. 指定 degree = 5，多项式只有6项，对应系数为6，图形的拟合度有明显提升。
reg = np.polyfit(x, f(x), deg=7)
print(reg)

# 根据最有系数，使用不同的x值进行回归计算。
ry = np.polyval(reg, x)

print(np.allclose(f(x), ry))
print(np.sum((f(x) - ry) ** 2) / len(x))

#plt.rc('grid', linestyle="--", color='black')
plt.plot(x, f(x), 'b', label='f(x)')
plt.plot(x, ry, 'r.', label='regression')
plt.legend(loc=0)
plt.grid(True)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

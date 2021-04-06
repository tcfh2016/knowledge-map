import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5*x

# 通过生成服从[0,1)均匀分布的随机数随机值来获取无序的x坐标值但值的范围处于[-2pi, 2pi)
# 的随机数
xu = np.random.rand(50) * 4 * np.pi - 2 * np.pi
yu = f(xu)
print(xu)
print(yu)


# 求解多项式最小二乘法解
reg = np.polyfit(xu, yu, 7)
print(reg)

# 根据如上得到的回归系数，使用x坐标值进行回归计算。
ry = np.polyval(reg, xu)
print(ry)

print(np.allclose(f(xu), ry))
print(np.sum((f(xu) - ry) ** 2) / len(xu))

#plt.rc('grid', linestyle="--", color='black')
plt.plot(xu, yu, 'b^', label='f(xu)')
plt.plot(xu, ry, 'ro', label='regression')
plt.legend(loc=0)
plt.grid(True)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

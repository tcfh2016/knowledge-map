import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5*x

# 原始坐标值，均匀分布
x = np.linspace(-2*np.pi, 2*np.pi, 50)
y = f(x)

# 分别给x坐标值，y坐标值添加噪声
xn = x + 0.15 * np.random.standard_normal(len(x))
yn = f(xn) + 0.25 * np.random.standard_normal(len(xn))

# 求解多项式最小二乘法解
reg = np.polyfit(xn, yn, 7)
print(reg)

# 根据如上得到的回归系数，使用x坐标值进行回归计算。
ry = np.polyval(reg, xn)
print(ry)

print(np.allclose(f(xn), ry))
print(np.sum((f(xn) - ry) ** 2) / len(xn))

#plt.rc('grid', linestyle="--", color='black')
plt.plot(x, y, 'g', label='f(x)')
plt.plot(xn, yn, 'b^', label='f(xn) with noise')
plt.plot(xn, ry, 'ro', label='regression')
plt.legend(loc=0)
plt.grid(True)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

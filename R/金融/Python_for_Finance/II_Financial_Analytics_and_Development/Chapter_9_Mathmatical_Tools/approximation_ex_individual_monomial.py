import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5*x

x = np.linspace(-2*np.pi, 2*np.pi, 50)

# 基于x坐标值创建不同幂次的数组
matrix = np.zeros((3 + 1, len(x)))
#使用幂次函数来求取最小二乘法的值误差较大，将其替换为sin()函数。
#matrix[3, :] = x ** 3
matrix[3, :] = np.sin(x)
matrix[2, :] = x ** 2
matrix[1, :] = x
matrix[0, :] = 1

# 使用线性代数库解决最小二乘法
reg = np.linalg.lstsq(matrix.T, f(x))[0]
print(reg)

# 根据最有系数，使用不同的x值进行回归计算。
ry = np.dot(reg, matrix)
print(ry)

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

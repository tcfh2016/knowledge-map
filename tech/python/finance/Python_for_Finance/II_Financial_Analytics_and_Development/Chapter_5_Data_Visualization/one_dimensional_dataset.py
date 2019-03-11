import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(1000)
y = np.random.standard_normal(20)
x = range(len(y))
print(y)

plt.plot(x, y)
plt.plot(y.cumsum(), 'ro') # 设置颜色为红色，样式为圆形。
plt.grid(True) # 添加网格
plt.axis('tight') # 调整坐标宽度
plt.xlim(-1, 20)  # 设置x轴值显示范围
plt.ylim(np.min(y.cumsum()) - 1, np.max(y.cumsum()) + 1) # 设置y轴值显示范围
plt.xlabel('index') # 设置x轴标签
plt.ylabel('value') # 设置x轴标签
plt.title('A Simple Plot') # 设置图形标题
plt.show()

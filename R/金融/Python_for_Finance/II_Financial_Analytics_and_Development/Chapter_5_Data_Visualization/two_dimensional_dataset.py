import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((20, 2))
print(y)

fig = plt.figure(figsize=(7, 4)) # 设置图形大小

ax1 = fig.subplots()
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro') # 设置颜色为红色，样式为圆形。
plt.legend(loc=8)

ax2 = ax1.twinx()
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro') # 设置颜色为红色，样式为圆形。
plt.legend(loc=0) # 使用legend, loc设置位置
plt.ylabel('value 2nd') # 第二个y坐标

plt.grid(True) # 添加网格
plt.axis('tight') # 调整坐标宽度
plt.xlabel('index') # 设置x轴标签
plt.ylabel('value') # 设置x轴标签
plt.title('A Simple Plot') # 设置图形标题
plt.show()

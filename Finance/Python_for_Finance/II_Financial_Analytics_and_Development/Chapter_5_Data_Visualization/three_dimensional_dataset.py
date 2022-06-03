import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((1000, 2))
c = np.random.randint(0, 10, len(y))

fig = plt.figure(figsize=(7, 5)) # 设置图形大小
plt.scatter(y[:, 0], y[:, 1], c=c, marker='o')
plt.colorbar()

plt.grid(True) # 添加网格
plt.axis('tight') # 调整坐标宽度
plt.xlabel('index') # 设置x轴标签
plt.ylabel('value') # 设置x轴标签
plt.title('Scatter Plot') # 设置图形标题
plt.show()

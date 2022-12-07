import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((1000, 2))

plt.figure(figsize=(7, 4))
plt.hist(y, label=['1st', '2nd'], color=['b', 'g'], stacked=True, bins=20)

plt.grid(True) # 添加网格
plt.legend(loc=0)
plt.axis('tight') # 调整坐标宽度
plt.xlabel('value') # 设置x轴标签
plt.ylabel('frequency') # 设置x轴标签
plt.title('Histogram') # 设置图形标题
plt.show()

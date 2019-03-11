## Chapter 5. Data Visualization

matplotlib是与NumPy兼容良好的可视化函数库。

### Two-Dimensional Plotting

1.One-Dimensional Data Set

绘图相关函数主要存在于matplotlib的子函数库matplotlib.pyplot里， 绘图函数为plot。

```
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
```

绘图时候需要同时传入x, y轴的数据（支持list和array），当省略x轴的数据时默认将y轴数据的索
引当作x轴引用数据。plot能够支持ndarray，但谨防传入过于复杂的数据。与此同时，matplotlib
提供了许多函数来自定义绘图的各种样式。

- plt.grid(True)    # 添加网格
- plt.axis('tight') # 调整坐标宽度
- plt.xlim(-1, 20)  # 设置x轴值显示范围
- plt.ylim(np.min(y.cumsum()) - 1, np.max(y.cumsum()) + 1) # 设置y轴值显示范围
- plt.xlabel('index') # 设置x轴标签
- plt.ylabel('value') # 设置x轴标签
- plt.title('A Simple Plot') # 设置图形标题
- plt.plot(y.cumsum(), 'ro') # 设置颜色为红色，样式为圆形。

2.Two-Dimensional Data Set

如下使用random生成的二维伪随机序列，matplotlib会将其识别为两个数据集，因此会绘制两条线。

```
y = np.random.standard_normal((20, 2))

plt.figure(figsize=(7, 4)) # 设置图形大小
plt.plot(y, 'ro') # 设置颜色为红色，样式为圆形。
plt.plot(y[:, 0], lw=1.5, label='1st') # 设置第1列数据集的标签为1st。
plt.plot(y[:, 1], lw=1.5, label='2nd') # 设置第1列数据集的标签为2nd。
plt.legend(loc=0) # 使用legend, loc设置位置
```

二维的数字集合的展示会面临两个问题：一、两者拥有不同的数量级因此很难用相同的坐标来展示；
二、使用不同的样式来分别展示它们。有两种解决方案可以用来解决这个问题：

- 使用两个y坐标轴
- 绘制子图
